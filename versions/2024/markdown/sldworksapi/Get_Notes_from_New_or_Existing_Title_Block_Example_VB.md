---
title: "Get Notes from New or Existing Title Block (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm"
---

# Get Notes from New or Existing Title Block (VBA)

This example shows how to create a title block in a drawing, if one
does not already exist, and how to get the notes from an existing title
block in a drawing.

```vb
'--------------------------------------------------------
' Preconditions: Drawing document is open.
'
' Postconditions: If the drawing contains a title block, then
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}notes of that block are printed
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}to the Immediate window. If not, then
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}a title block is created.
'-------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As ModelDoc2
Dim swExt As ModelDocExtension
Dim swSelMgr As SelectionMgr
Dim swView As View
Dim swDraw As DrawingDoc

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swExt = swModel.Extension
Set swSelMgr = swModel.SelectionManager

Set swDraw = swModel

Dim swSheet As Sheet
Set swSheet = swDraw.GetCurrentSheet

Dim swTitleBlock As TitleBlock
Set swTitleBlock = swSheet.TitleBlock

Dim vNotes As Variant
Dim i As Integer
' Create title block if one doesn't exist
If swTitleBlock Is Nothing Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swView = swDraw.GetFirstView
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vNotes = swView.GetNotes
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Add first two notes to the title block
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim notesArray(1) As Object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set notesArray(0) = vNotes(0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set notesArray(1) = vNotes(1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swTitleBlock = swSheet.InsertTitleBlock(notesArray)
kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}
End If

vNotes = swTitleBlock.GetNotes

For i = 0 To UBound(vNotes)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swNote As Note
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swNote = vNotes(i)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Name: " & swNote.GetName
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Value: " & swNote.GetText
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
Next
End Sub
```
