---
title: "Set Body for View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Body_for_View_Example_VBNET.htm"
---

# Set Body for View Example (VB.NET)

This example shows how to show just one body of a multibody part in
a drawing view.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi_inter.sldprt.
' 2. Save the part document as a drawing document:
'    a. Click File > Make Drawing from Part.
'    b. Click OK on the Sheet Format/Size dialog.
'    c. Drag the *Isometric view from the View Palette onto
'       the drawing sheet.
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
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swView As View
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrBodies As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim arrBody As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swBody As Body2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFace As Face2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swEnt As Entity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelData As SelectData
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bool As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim arrBodiesIn(0) As DispatchWrapper
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Bodies(0) As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim objType As Long

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swView = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (swView Is Nothing) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("View not selected.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrBodies = swView.GetBodiesCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Number of bodies: " & nbrBodies)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (nbrBodies < 1) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("No bodies in selected view.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}arrBody = swView.Bodies
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(arrBody)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swBody = arrBody(i)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelData = swSelMgr.CreateSelectData
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelData.View = swView
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool = swBody.Select2(False, swSelData)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Object type 76 is a solid body
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}objType = swSelMgr.GetSelectedObjectType3(1, -1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If (objType = 76) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Object type: solid body")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If (Not (swSelectType_e.swSelSOLIDBODIES = swSelMgr.GetSelectedObjectType3(1, -1))) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}MsgBox("Solid body not found.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFace = swBody.GetFirstFace
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Do While Not swFace Is Nothing
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swEnt = swFace
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Select using IEntity
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}bool = swEnt.Select4(True, swSelData) : Debug.Assert(bool)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFace = swFace.GetNextFace
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Loop
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Name of body: " & swBody.GetSelectionId)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the bodies from referenced model
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swView.ReferencedDocument
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}arrBody = swModel.GetBodies2(swBodyType_e.swSolidBody, True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (nbrBodies = 1) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView.Bodies = (arrBody)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Set the body to include in the drawing view
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Bodies(0) = arrBody(0)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}arrBodiesIn(0) = New DispatchWrapper(Bodies(0))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView.Bodies = (arrBodiesIn)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
