---
title: "IImprintingFacesCount Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "IImprintingFacesCount"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~IImprintingFacesCount.html"
---

# IImprintingFacesCount Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function IImprintingFacesCount( _
   ByVal NTargetFaces As Long, _
   ByVal TargetFaceArray As Face, _
   ByVal NToolFaces As Long, _
   ByVal ToolFaceArray As Face, _
   ByVal Options As Long, _
   ByRef NTargetEdges As Long, _
   ByRef NtoolEdges As Long, _
   ByRef NtargetVertices As Long, _
   ByRef ToolVertices As Long _
) As Boolean
```
