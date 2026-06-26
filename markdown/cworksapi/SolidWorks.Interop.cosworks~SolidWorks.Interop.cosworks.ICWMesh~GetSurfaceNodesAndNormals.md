---
title: "GetSurfaceNodesAndNormals Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetSurfaceNodesAndNormals"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSurfaceNodesAndNormals.html"
---

# GetSurfaceNodesAndNormals Method (ICWMesh)

Gets the nodes and normal vectors at the surface of this solid mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSurfaceNodesAndNormals( _
   ByRef VarNodeIDs As System.Object, _
   ByRef VarNumNormals As System.Object, _
   ByRef VarNormalVecs As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim VarNodeIDs As System.Object
Dim VarNumNormals As System.Object
Dim VarNormalVecs As System.Object
Dim value As System.Integer

value = instance.GetSurfaceNodesAndNormals(VarNodeIDs, VarNumNormals, VarNormalVecs)
```

### C#

```csharp
System.int GetSurfaceNodesAndNormals(
   out System.object VarNodeIDs,
   out System.object VarNumNormals,
   out System.object VarNormalVecs
)
```

### C++/CLI

```cpp
System.int GetSurfaceNodesAndNormals(
   [Out] System.Object^ VarNodeIDs,
   [Out] System.Object^ VarNumNormals,
   [Out] System.Object^ VarNormalVecs
)
```

### Parameters

- `VarNodeIDs`: Array of node IDs (see

Remarks

)
- `VarNumNormals`: Array of numbers (1, 2 or 3) of normal vectors for the corresponding node ID in VarNodeIDs (see

Remarks

)
- `VarNormalVecs`: Array of normal vectors (see

Remarks

)

### Return Value

Number of nodes

## VBA Syntax

See

[CWMesh::GetSurfaceNodesAndNormals](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetSurfaceNodesAndNormals.html)

.

## Examples

[Get Mesh Elements and Nodes (VBA)](Get_Mesh_Elements_and_Nodes_Example_VB.htm)

[Get Mesh Elements and Nodes (VB.NET)](Get_Mesh_Elements_and_Nodes_Example_VBNET.htm)

[Get Mesh Elements and Nodes (C#)](Get_Mesh_Elements_And_Nodes_Example_CSharp.htm)

## Remarks

You must set[ICWMesh::Quality](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~Quality.html)to[swsMeshQuality_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshQuality_e.html).swsMeshQualityHigh before calling this method.

Each node can have one or more normal vectors. For example, for a meshed cube:

| Node location | Number of normal vectors |
| --- | --- |
| Middle of side | 1 |
| Edge | 2 |
| Vertex | 3 |

VarNormalVecs contains an array of all of the normal vectors:

[

`xa 1 , ya 1 , za 1 , xb 1 , yb 1 , zb 1 , xc 1 , yc 1 , zc 1 ,`

`xa 2 , ya 2 , za 2 ,`

`...,`

`xa i , ya i , za i`

]

where:

- x

  ,

  y

  , and

  z

  denote location
- a

  ,

  b

  , and

  c

  denote normal vectors
- xa

  i

  ,

  ya

  i

  ,

  za

  i

  denote the location of the

  a

  th

  normal vector for the

  i

  th

  node

Use VarNumNormals to calculate which vectors in VarNormalVecs map to the node IDs in VarNodeIDs.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)

[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

[ICWMesh::GetElementList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementList.html)

[ICWMesh::GetNodeList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeList.html)

[ICWMesh::GetSolidElementList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidElementList.html)

[ICWMesh::GetSolidNodeList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidNodeList.html)

## Availability

SOLIDWORKS Simulation API 2016 SP05
