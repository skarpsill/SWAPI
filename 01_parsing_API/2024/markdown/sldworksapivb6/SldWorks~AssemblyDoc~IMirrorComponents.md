---
title: "IMirrorComponents Method (AssemblyDoc)"
project: "SOLIDWORKS Type Library"
interface: "AssemblyDoc"
member: "IMirrorComponents"
kind: "method"
source: "sldworksapivb6/SldWorks~AssemblyDoc~IMirrorComponents.html"
---

# IMirrorComponents Method (AssemblyDoc)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function IMirrorComponents( _
   ByVal Plane As Object, _
   ByVal InstanceCount As Long, _
   ByVal ComponentsToInstance As Component2, _
   ByVal MirrorCount As Long, _
   ByVal ComponentsToMirror As Component2, _
   ByVal NameCount As Long, _
   ByRef MirroredComponentFilenames As String, _
   ByVal RecreateMates As Boolean, _
   ByVal ComponentModifier As Long, _
   ByVal ComponentNameModifier As String, _
   ByVal MirroredFileLocation As String, _
   ByVal CopyCustomProperties As Boolean _
) As Component2
```
