---
title: "Set Body for View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Body_for_View_Example_VB.htm"
---

# Set Body for View Example (VBA)

This example shows how to show just one body of a multibody part in
a drawing view.

```vb
'------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
 ' 2. Save the part document as a drawing document:
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click File > Make Drawing from Part.
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Click OK on the Sheet Format/Size dialog.
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Drag the *Isometric view from the View Palette onto
 ' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}the drawing sheet.
 ' 3. Select the drawing view.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Shows one body of the multibody part
 '    in the drawing view.
 ' 2. Examine the drawing and the Immediate window.
 '
 ' NOTE: Because the part document is used elsewhere, do not save
 ' changes.
 '------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim nbrBodies As Long
Dim arrBody As Variant
Dim swBody As SldWorks.Body2
Dim swFace As SldWorks.Face2
Dim swEnt As SldWorks.Entity
Dim swSelData As SldWorks.SelectData
Dim bool As Boolean
Dim arrBodiesIn As Variant
Dim Bodies(0) As Object
Dim i As Long
Dim objType As Long

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swView = swSelMgr.GetSelectedObject6(1, -1)
If (swView Is Nothing) Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}MsgBox "View not selected."
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Exit Sub
End If
nbrBodies = swView.GetBodiesCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Number of bodies: " & nbrBodies
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If (nbrBodies < 1) Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox "No bodies in selected view."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
arrBody = swView.Bodies
For i = 0 To UBound(arrBody)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swBody = arrBody(i)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSelData = swSelMgr.CreateSelectData
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSelData.View = swView
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}bool = swBody.Select2(False, swSelData)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Object type 76 is a solid body
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}objType = swSelMgr.GetSelectedObjectType3(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (objType = 76) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print " Object type: solid body"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (Not (swSelSOLIDBODIES = swSelMgr.GetSelectedObjectType3(1, -1))) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox "Solid body not found."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swFace = swBody.GetFirstFace
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Do While Not swFace Is Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swEnt = swFace
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Select using IEntity
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool = swEnt.Select4(True, swSelData): Debug.Assert bool
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swFace = swFace.GetNextFace
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Loop
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Name of body: " & swBody.GetSelectionId
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{</spaces>}}
swModel.ClearSelection2 True

' Get the bodies from referenced model
Set swModel = swView.ReferencedDocument
arrBody = swModel.GetBodies2(swSolidBody, True)
If (nbrBodies = 1) Then
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}swView.Bodies = (arrBody)
Else
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Set the body to view
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set Bodies(0) = arrBody(0)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}arrBodiesIn = Bodies
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}swView.Bodies = (arrBodiesIn)
End If

swModel.ClearSelection2 True
```

```vb
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
```
