---
title: "Get Section Properties for Planar Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Section_Properties_Example2_VB.htm"
---

# Get Section Properties for Planar Faces Example (VBA)

This example shows how to get section properties for planar faces.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a part that has at least three planar faces.
' 2. Select three planar faces.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the section properties of the three selected
'    faces.
' 2. Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim boolstatus As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModelDoc = swApp.ActiveDoc
Set swModelDocExt = swModelDoc.Extension
Set swSelMgr = swModelDoc.SelectionManager
```

```
boolstatus = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
Dim face1(0 To 0) As Object
Set face1(0) = swSelMgr.GetSelectedObject5(1)
swModelDoc.ClearSelection2 True
Dim vFace1 As Variant
vFace1 = face1
Dim v1 As Variant
```

```
Debug.Print "Section properties:"
```

```
' Get the section properties for the selected face
v1 = swModelDocExt.GetSectionProperties2((vFace1))
Dim i As Integer
Debug.Print "  First selected face:"
For i = 0 To UBound(v1)
    Debug.Print "    " & v1(i); ""
Next i
```

```
boolstatus = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
Dim face2(0 To 0) As Object
Set face2(0) = swSelMgr.GetSelectedObject5(1)
swModelDoc.ClearSelection2 True
Dim vFace2 As Variant
vFace2 = face2
Dim v2 As Variant
```

```
' Get the section properties for the selected face
v2 = swModelDocExt.GetSectionProperties2((vFace2))
Debug.Print "  Second selected face:"
For i = 0 To UBound(v1)
    Debug.Print "    " & v1(i)
Next i
boolstatus = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
Dim face3(0 To 0) As Object
Set face3(0) = swSelMgr.GetSelectedObject5(1)
swModelDoc.ClearSelection2 True
Dim vFace3 As Variant
vFace3 = face3
Dim v3 As Variant
```

```
' Get the section properties for the selected face
v3 = swModelDocExt.GetSectionProperties2((vFace3))
Debug.Print "  Third selected face:"
For i = 0 To UBound(v1)
    Debug.Print "    " & v1(i)
Next i
```

```
End Sub
```
