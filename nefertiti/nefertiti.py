from array import array
from base64 import b64encode, b64decode

vertices = []
maxV = 0
minV = 0
indices = []
with open("Nefertiti.obj") as f:
    for line in f:
        line = line.split(" ")
        if line[0] == "v":
            line = [float(a) for a in line[1:]]
            for i in line:
                if i < minV:
                    minv = i
                if i > maxV:
                    maxV = i
            vertices.extend(line)
        elif line[0] == "f":
            line = [int(a) - 1 for a in line[1:]]
            indices.extend(line)

if abs(minV) > maxV:
    maxV = abs(minV)
vertices = map(lambda a: a / maxV, vertices)

#for i in indices:
#    faces.append(vertices[i])
vertices = b64encode(array('f', vertices))
indices = b64encode(array('L', indices))
#faces = b64encode(array('f', faces))

print('const vertices="%s"' % vertices.decode('ascii'))
print('const indices="%s"' % indices.decode('ascii'))
#print('const faces="%s"' % faces.decode('ascii'))
