# 간단한 분자 구조 그리는 프로그램 예제

from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image,ImageTk
import pubchempy as pcp
import pandas as pd
import cv2


def Name2Smiles(mol : str = None):
    timeout = 60
    compounds = pcp.get_compounds(mol, 'name', timeout=timeout)
    if compounds:
        compound = compounds[0]
        return compound.isomeric_smiles

mol = input()

smiles = Name2Smiles(mol)
molecule = Chem.MolFromSmiles(smiles)

img = Draw.MolToImage(molecule)

img.save('img.png')

img = cv2.imread('img.png')
cv2.imshow('MAP',img)

cv2.waitKey(0)
cv2.destroyAllWindows()