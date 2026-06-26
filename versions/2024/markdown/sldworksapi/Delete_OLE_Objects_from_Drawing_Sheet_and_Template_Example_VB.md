---
title: "Delete OLE Objects from Drawing Sheet and Template Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_OLE_Objects_from_Drawing_Sheet_and_Template_Example_VB.htm"
---

# Delete OLE Objects from Drawing Sheet and Template Example (VBA)

This example shows how to delete any OLE objects from the current drawing
sheet and template.

```
'---------------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains one or more
'    OLE objects in the drawing sheet or template.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Deletes all OLE objects in drawing sheet
'    and template.
' 2. Examine the graphics area and Immediate window.
'--------------------------------------------------------
```

Option Explicit

Sub DeleteAllOleItemsInSheet _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
As SldWorks.SldWorks, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
As SldWorks.ModelDoc2, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSheet
As SldWorks.Sheet _

)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nOleCntkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nSizekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nAspectkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
skArray()kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nOleCnt
= swSheet.GetOLEObjectCount: If
0 = nOleCnt Then Exit Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
skArray(nOleCnt - 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get location of each OLE item

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To nOleCnt - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}skArray(i)
= swSheet.GetOLEObjectSettings(i,
nSize, nAspect)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Delete each OLE items

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To nOleCnt - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swModel.SelectByID("",
"OLEITEM",kadov_tag{{</spaces>}}0.5
* (skArray(i)(0) + skArray(i)(3)),kadov_tag{{</spaces>}}0.5
* (skArray(i)(1) + skArray(i)(4)),kadov_tag{{</spaces>}}0.5
* (skArray(i)(2) + skArray(i)(5)))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swModel.DeleteSelection(False)
Debug.Print ("OLE item " & i & "
deleted? " & bRet)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSheetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSheet = swDraw.GetCurrentSheetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DeleteAllOleItemsInSheet
swApp, swModel, swSheet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Switch to template and delete OLE objects

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDraw.EditTemplate

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSheet = swDraw.GetCurrentSheet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DeleteAllOleItemsInSheet
swApp, swModel, swSheet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDraw.**EditSheet**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Switch back to sheet and make sure all OLE objects are deleted

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSheet = swDraw.GetCurrentSheet

kadov_tag{{<spaces>}}

End Sub
