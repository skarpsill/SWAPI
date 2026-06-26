---
title: "Delete Selected Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Selected_Faces_Example_VB.htm"
---

# Delete Selected Faces Example (VBA)

This example shows how to delete selected faces.

```
'------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Select the cylindrical faces.
'
' Postconditions:
' 1. Deletes the cylindrical faces, but does not fill
'    in the deleted cylindrical faces. Also, creates a
'    a DeleteFace feature.
' 2. Examine the graphics area and FeatureManager
'    design tree.
'
' NOTE: Because this part is used elsewhere, do not
' save changes.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' IModelDoc2::InsertDeleteFace2 only works for parts
    '   1 refills the face after it is deleted
    '   0 does not
    bRet = swModel.InsertDeleteFace2(0)
```

```
End Sub
```
