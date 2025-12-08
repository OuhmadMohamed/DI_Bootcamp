#!/usr/bin/env python3
"""
detect_isolate_face.py

Usage:
    python detect_isolate_face.py --image chemin/vers/image.jpg [--out visage.npy] [--save-img visage.png] [--no-display]

Fonctions:
 - charge une image (vérifie existence et format)
 - détecte les visages avec OpenCV (cascade Haar)
 - isole (crop) le premier visage détecté -> numpy.ndarray dtype=uint8, shape (h, w, 3)
 - sauvegarde la matrice avec numpy.save()
 - affiche l'image originale (rectangle) et le crop
 - optionnel: si mediapipe est installé, calcule des landmarks et estime une expression simple
"""
import argparse
import os
import sys
from typing import Tuple, Optional

import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

# Path vers le classifieur en cascade fourni par OpenCV (installé avec opencv-python)
HAAR_CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

def load_image(path: str) -> np.ndarray:
    """Charge une image couleur en BGR avec OpenCV. Lève ValueError si échec."""
    if not os.path.isfile(path):
        raise ValueError(f"Le fichier n'existe pas : {path}")
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"Impossible de charger l'image (format non supporté ou fichier corrompu) : {path}")
    return img

def detect_faces_opencv(img_bgr: np.ndarray,
                        scaleFactor: float = 1.1,
                        minNeighbors: int = 5,
                        minSize: Tuple[int, int] = (30, 30)) -> list:
    """Détecte visages avec Haar Cascade. Retourne liste de (x,y,w,h)."""
    if not os.path.exists(HAAR_CASCADE_PATH):
        raise RuntimeError(f"Fichier cascade non trouvé : {HAAR_CASCADE_PATH}")
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
    return faces.tolist() if len(faces) else []

def crop_face(img_bgr: np.ndarray, bbox: Tuple[int, int, int, int],
              pad: int = 0) -> np.ndarray:
    """Recadre l'image selon bbox = (x,y,w,h). Gère les bords et renvoie crop couleur (h,w,3) dtype=uint8."""
    x, y, w, h = bbox
    h_img, w_img = img_bgr.shape[:2]
    x1 = max(0, x - pad)
    y1 = max(0, y - pad)
    x2 = min(w_img, x + w + pad)
    y2 = min(h_img, y + h + pad)
    crop = img_bgr[y1:y2, x1:x2].copy()
    # Assure la forme (H,W,3) et dtype uint8
    if crop.ndim == 2:
        # cas improbable : image gris ; convertir en 3 canaux
        crop = cv2.cvtColor(crop, cv2.COLOR_GRAY2BGR)
    if crop.dtype != np.uint8:
        crop = crop.astype(np.uint8)
    return crop

def save_numpy(arr: np.ndarray, filename: str) -> None:
    """Sauvegarde en .npy et affiche la forme et le nom de fichier créé."""
    np.save(filename, arr)
    print(f"[INFO] Matrice sauvegardée : {filename}")
    print(f"[INFO] Shape : {arr.shape}, dtype : {arr.dtype}")

# --- Bonus MediaPipe (optionnel) ---
try:
    import mediapipe as mp
    _HAS_MEDIAPIPE = True
except Exception:
    _HAS_MEDIAPIPE = False

def analyze_expression_with_mediapipe(bgr_face: np.ndarray) -> Optional[str]:
    """
    Analyse sommaire avec MediaPipe FaceMesh si disponible.
    Retourne une estimation simple : 'heureux', 'surpris', 'neutre' ou None si mediapipe absent.
    NOTE: heuristique simple basée sur ouverture de la bouche et inclinaison des coins.
    """
    if not _HAS_MEDIAPIPE:
        return None

    mp_face_mesh = mp.solutions.face_mesh
    # Nous utilisons face_mesh sur l'image recadrée. Convertir en RGB pour mediapipe.
    rgb = cv2.cvtColor(bgr_face, cv2.COLOR_BGR2RGB)
    with mp_face_mesh.FaceMesh(static_image_mode=True,
                               max_num_faces=1,
                               refine_landmarks=False,
                               min_detection_confidence=0.5) as fm:
        results = fm.process(rgb)
        if not results.multi_face_landmarks:
            return None
        lm = results.multi_face_landmarks[0].landmark
        h, w = bgr_face.shape[:2]

        # Indices communs utilisés par la communauté FaceMesh (approx.)
        # bouche : coin gauche 61, coin droit 291, lèvre sup 13, lèvre inf 14
        try:
            def pt(idx):
                return np.array([lm[idx].x * w, lm[idx].y * h])
            left_corner = pt(61)
            right_corner = pt(291)
            top_lip = pt(13)
            bottom_lip = pt(14)

            mouth_width = np.linalg.norm(right_corner - left_corner)
            mouth_open = np.linalg.norm(bottom_lip - top_lip)

            # ratio d'ouverture
            if mouth_width == 0:
                return "neutre"
            ratio = mouth_open / mouth_width

            # heuristique : seuils empiriques — peuvent demander ajustement
            if ratio > 0.35:
                return "surpris"
            elif ratio > 0.12:
                return "heureux"
            else:
                return "neutre"
        except Exception:
            return None

def draw_rectangle(img: np.ndarray, bbox: Tuple[int, int, int, int], label: Optional[str] = None) -> None:
    """Dessine rectangle et label (texte) sur l'image (BGR)"""
    x, y, w, h = map(int, bbox)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if label:
        cv2.putText(img, label, (x, max(0, y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

def main():
    parser = argparse.ArgumentParser(description="Détection et isolement d'un visage (OpenCV).")
    parser.add_argument("--image", type=str, default=r'C:\Users\admin\Documents\python_ex\images\images.jpg', help="Chemin vers l'image d'entrée.")
    parser.add_argument("--out", "-o", default="visage.npy", help="Nom du fichier .npy de sortie.")
    parser.add_argument("--save-img", default=None, help="Optionnel : sauvegarder le crop en image (.png/.jpg).")
    parser.add_argument("--no-display", action="store_true", help="Ne pas afficher les fenêtres OpenCV (utile pour serveurs).")
    parser.add_argument("--pad", type=int, default=10, help="Padding en pixels autour de la bounding box (optionnel).")
    args = parser.parse_args()

    try:
        img = load_image(args.image)
    except ValueError as e:
        print(f"[ERREUR] {e}")
        sys.exit(1)

    faces = detect_faces_opencv(img)
    if not faces:
        print("[INFO] Aucun visage détecté dans l'image.")
        sys.exit(0)

    # Traiter au minimum le premier visage détecté
    bbox = faces[0]  # x, y, w, h
    print(f"[INFO] Visages détectés : {len(faces)}. Traitement du 1er visage : {bbox}")

    # Crop et conversion en numpy.ndarray (déjà l'est)
    face_crop = crop_face(img, bbox, pad=args.pad)

    # Sauvegarde en .npy
    # Vérifie que la matrice a la forme attendue (H, W, 3) et dtype uint8
    if face_crop.ndim == 2:
        face_crop = cv2.cvtColor(face_crop, cv2.COLOR_GRAY2BGR)
    if face_crop.shape[2] != 3:
        # for safety, convert/truncate/pad channels
        face_crop = face_crop[:, :, :3]

    face_crop = face_crop.astype(np.uint8)
    save_numpy(face_crop, args.out)

    # Optionnel : MediaPipe analyse
    expression = None
    if _HAS_MEDIAPIPE:
        expression = analyze_expression_with_mediapipe(face_crop)
        if expression:
            print(f"[BONUS] Expression estimée (MediaPipe heuristique) : {expression}")

    # Affichage
    annotated = img.copy()
    label = f"Visage 1"
    if expression:
        label += f" | {expression}"
    draw_rectangle(annotated, bbox, label=label)

    if args.save_img:
        # sauvegarde du crop en image
        try:
            cv2.imwrite(args.save_img, face_crop)
            print(f"[INFO] Crop sauvegardé en image : {args.save_img}")
        except Exception as e:
            print(f"[WARN] Impossible de sauvegarder l'image : {e}")

    if not args.no_display:
        # Affiche image originale annotée et le crop
        cv2.imshow("Original (annoté)", annotated)
        cv2.imshow("Visage isolé", face_crop)
        print("[INFO] Appuyez sur une touche dans la fenêtre d'image pour fermer.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("[INFO] Option --no-display active : affichage désactivé.")

if __name__ == "__main__":
    main()
