import igl
import numpy as np
import meshplot as mp
from fem_laplace import fem_laplacian
import trimesh as tm
import matplotlib.pyplot as plt
import io
from PIL import Image

MODELO = 'ArteryObjAN1-15'
v_og, f_og = igl.read_triangle_mesh("originales/" + MODELO + '.obj')
v_gen, f_gen = igl.read_triangle_mesh("generadas/" + MODELO + '.off')

evalues_og, evectors_og = fem_laplacian( v_og, f_og, normalization='None', verbose=True, spectrum_size=30)
evalues_gen, evectors_gen = fem_laplacian( v_gen, f_gen, normalization='None', verbose=True, spectrum_size=30)

mesh = tm.Trimesh(vertices=v_og,faces=f_og )
mesh.visual.vertex_colors = tm.visual.interpolate(evectors_og[:,0] * evalues_og[0], color_map='viridis')
scene = tm.Scene(mesh)
data = scene.save_image(resolution=[1920, 1080])

image = np.array(Image.open(io.BytesIO(data))) 
plt.imshow(image)