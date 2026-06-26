---
title: "GetElements Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetElements"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElements.html"
---

# GetElements Method (ICWMesh)

Gets the elements of the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElements() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Object

value = instance.GetElements()
```

### C#

```csharp
System.object GetElements()
```

### C++/CLI

```cpp
System.Object^ GetElements();
```

### Return Value

Array of the elements of the mesh (see

Remarks

)

## VBA Syntax

See

[CWMesh::GetElements](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetElements.html)

.

## Remarks

Probe functionality.

Array of element data:

[

`E 1 , N 1 E 1 , N 2 E 1 , N 3 E 1 , N 4 E 1 , N 5 E 1 , N 6 E 1 , N 7 E 1 , N 8 E 1 , N 9 E 1 , N 10 E 1 , X 1 , Y 1 , Z 1 , AR 1 , JR 1 ,`

`E 2 , N 1 E 2 , N 2 E 2 , N 3 E 2 , N 4 E 2 , N 5 E 2 , N 6 E 2 , N 7 E 2 , N 8 E 2 , N 9 E 2 , N 10 E 2 , X 2 , Y 2 , Z 2 , AR 2 , JR 2 ,`

`...,`

`E i , N 1 E i , N2E i , N3E i , N4E i , N5E i , N6E i , N7E i , N8E i , N9E i , N10E i , X i , Y i , Z i , AR i , JR i`

]

where:

- E

  i

  =

  i

  th

  element number
- N

  1

  E

  i

  to N

  10

  E

  i

  = Node numbers associated with element E

  i

  ; returns 10 node numbers for higher order solid elements; returns -1 for shells and lower order meshes.
- X

  i

  , Y

  i

  , Z

  i

  = x, y and z coordinates of center of E

  i
- AR

  i

  kadov_tag{{<spaces>}}

  kadov_tag{{</spaces>}}

  = Aspect ratio for element E

  i
- JR

  i

  kadov_tag{{<spaces>}}

  kadov_tag{{</spaces>}}

  = Jacobian ratio for element E

  i

  ; returns -1 if not applicable

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)

[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

[ICWMesh::GetDefaultElementSizeAndTolerance Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html)

[ICWMesh::GetElementDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementDataFromEntity.html)

[ICWMesh::GetElementLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementLocation.html)

[ICWMesh::ElementCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementCount.html)

[ICWMesh::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementSize.html)

[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)

[ICWMesh::MaxAspectRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxAspectRatio.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
