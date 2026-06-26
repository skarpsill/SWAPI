---
title: "Get Views and Notes(VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Views_and_Notes_Example_VB.htm"
---

# Get Views and Notes(VBA)

## Get Views and Notes (VBA)

This example shows how to get all of the views and notes in a drawing
document.

```vb
'--------------------------------------------
' Preconditions: Drawing document is open and at least
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}one view has some notes.
'
' Postconditions: None
'
' NOTE: IDrawingDoc::GetViews returns both sheets and views.
'----------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawDoc As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swNote As SldWorks.Note
Dim sheetCount As Long
Dim viewCount As Long
Dim noteCount As Long
Dim i As Long

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swDrawDoc = swModel

Dim viewCount As Long
viewCount = swDrawDoc.GetViewCount

Dim ss As Variant
ss = swDrawDoc.GetViews

For sheetCount = LBound(ss) To UBound(ss)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vv As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vv = ss(sheetCount)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For viewCount = LBound(vv) To UBound(vv)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print (vv(viewCount).GetName2())

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vNotes As Variant
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}noteCount = vv(viewCount).GetNoteCount

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If noteCount > 0 Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vNotes = vv(viewCount).GetNotes
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For i = 0 To noteCount - 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Note text: " & vNotes(i).GetText
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next viewCount

Next sheetCount

End Sub
```
