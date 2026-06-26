---
title: "Get and Set Format of Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Format_of_Note_Example_VB.htm"
---

# Get and Set Format of Note Example (VBA)

This example shows how to the get and set the format of a selected note.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
' 2. Select the Fixed face note.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Reformats the selected note.
' 2. Click the drawing and examine the note.
' 3. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swNote As SldWorks.Note
Dim swSelMgr As SldWorks.SelectionMgr

Sub main()

   Set swApp = Application.SldWorks
   Set swModel = swApp.ActiveDoc
   Set swSelMgr = swModel.SelectionManager

   ' Get selected rich-text formatted note
   Set swNote = swSelMgr.GetSelectedObject6(1, 0)

   ' Print the current note including the formatting tags
   Debug.Print "Before reformatting: " & swNote.PropertyLinkedText

   ' Change the color of the selected note to red and bold
   ' all of the text
   swNote.PropertyLinkedText = "<FONT color=0x000000ff><FONT style=B>This is a test of formatting a note using the API"

   ' Print the current note including the formatting tags
   Debug.Print "After reformatting: " & swNote.PropertyLinkedText

   ' Rebuild the document to see the newly formatted note
   swModel.EditRebuild3

End Sub
```
