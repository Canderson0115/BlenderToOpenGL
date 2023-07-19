import sys
import argparse
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def subtract(a, b):
    return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]

def normalize(a):
    mag = math.sqrt(sum([x**2 for x in a]))
    return [x/mag for x in a]

def dot(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("obj_file", help="path to obj file")
    parser.add_argument("output_file", help="path to output text file")
    return parser.parse_args()

def read_obj_file(obj_file):
    vertices = []
    faces = []

    with open(obj_file, 'r') as f:
        for line in f:
            tokens = line.split()

            if not tokens:
                continue

            if tokens[0] == 'v':
                vertex = list(map(float, tokens[1:]))
                vertices.append(vertex)

            elif tokens[0] == 'f':
                # face_indices = list(map(int, reversed(tokens[1:])))
                # faces.append(face_indices)
                face_def = line.split()[1:]
                # Split each face definition into a list of vertex/texture/normal triplets
                face_triplets = [triplet.split('/') for triplet in face_def]
                # Extract only the vertex index for each triplet
                face_vertices = [int(triplet[0]) for triplet in face_triplets]
                faces.append(face_vertices)

    return vertices, faces

def write_opengl_file(output_file, vertices, faces):
    with open(output_file, 'w') as f:
        for face in faces:
            if len(face) == 3:
                vertex1 = vertices[face[0] - 1]
                vertex2 = vertices[face[1] - 1]
                vertex3 = vertices[face[2] - 1]

                normal = cross(subtract(vertex2, vertex1), subtract(vertex3, vertex1))
                normal = normalize(normal)

                f.write('glBegin(GL_TRIANGLES);\n')
                f.write(f'glNormal3f({normal[0]}, {normal[1]}, {normal[2]});\n')
                f.write(f'glVertex3f({vertex1[0]}, {vertex1[1]}, {vertex1[2]});\n')
                f.write(f'glVertex3f({vertex2[0]}, {vertex2[1]}, {vertex2[2]});\n')
                f.write(f'glVertex3f({vertex3[0]}, {vertex3[1]}, {vertex3[2]});\n')
                f.write('glEnd();\n')

            elif len(face) == 4:
                # handle quad faces
                # split the quad into two triangles
                vertex1 = vertices[face[0] - 1]
                vertex2 = vertices[face[1] - 1]
                vertex3 = vertices[face[2] - 1]
                vertex4 = vertices[face[3] - 1]

                normal1 = cross(subtract(vertex2, vertex1), subtract(vertex3, vertex1))
                normal1 = normalize(normal1)

                normal2 = cross(subtract(vertex4, vertex1), subtract(vertex3, vertex1))
                normal2 = normalize(normal2)

                f.write('glBegin(GL_TRIANGLES);\n')
                f.write(f'glNormal3f({normal1[0]}, {normal1[1]}, {normal1[2]});\n')
                f.write(f'glVertex3f({vertex1[0]}, {vertex1[1]}, {vertex1[2]});\n')
                f.write(f'glVertex3f({vertex2[0]}, {vertex2[1]}, {vertex2[2]});\n')
                f.write(f'glVertex3f({vertex3[0]}, {vertex3[1]}, {vertex3[2]});\n')
                f.write('glEnd();\n')

                f.write('glBegin(GL_TRIANGLES);\n')
                f.write(f'glNormal3f({normal2[0]}, {normal2[1]}, {normal2[2]});\n')
                f.write(f'glVertex3f({vertex1[0]}, {vertex1[1]}, {vertex1[2]});\n')
                f.write(f'glVertex3f({vertex3[0]}, {vertex3[1]}, {vertex3[2]});\n')
                f.write(f'glVertex3f({vertex4[0]}, {vertex4[1]}, {vertex4[2]});\n')
                f.write('glEnd();\n')

def main():
    args = parse_args()
    vertices, faces = read_obj_file(args.obj_file)
    write_opengl_file(args.output_file, vertices, faces)

if __name__ == '__main__':
    main()
