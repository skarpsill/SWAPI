---
title: "Get Notes from New or Existing Title Block (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm"
---

# Get Notes from New or Existing Title Block (VB.NET)

This example shows how to create a title block in a drawing, if one
does not already exist, and how to get the notes from an existing title
block in a drawing.

```vb
'--------------------------------------------------------
' Preconditions: Drawing document is open.
'
' Postconditions: If the drawing contains a title block, then
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}notes of that block are printed
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}to the Immediate window. If not, the a
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}title block is created.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swExt As ModelDocExtension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swView As View
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swDraw As DrawingDoc

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDraw = swModel

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSheet As Sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSheet = swDraw.GetCurrentSheet

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swTitleBlock As TitleBlock
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swTitleBlock = swSheet.TitleBlock

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vNotes As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create title block if one doesn't exist
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swTitleBlock Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = swDraw.GetFirstView
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vNotes = swView.GetNotes
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Add first two notes to the title block
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim notesArray(1) As DispatchWrapper
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}notesArray(0) = New DispatchWrapper(vNotes(0))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}notesArray(1) = New DispatchWrapper(vNotes(1))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swTitleBlock = swSheet.InsertTitleBlock(notesArray)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vNotes = swTitleBlock.GetNotes

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(vNotes)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim swNote As Note
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swNote = vNotes(i)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Name: " & swNote.GetName)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Value: " & swNote.GetText)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
