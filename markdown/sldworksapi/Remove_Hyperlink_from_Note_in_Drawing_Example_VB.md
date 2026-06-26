---
title: "Remove Hyperlink from Note in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Hyperlink_from_Note_in_Drawing_Example_VB.htm"
---

# Remove Hyperlink from Note in Drawing Example (VBA)

This example shows how to remove a hyperlink from a note in a drawing.

```
'-------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing to open exists.
' 2. Verify that you have internet connection.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Inserts a note containing a hyperlink to http://www.solidworks.com.
' 3. At Stop, click the note in the drawing, which opens the
'    SOLIDWORKS home web page.
' 4. Close the web page, close the Note PropertyManager page, and
'    click Continue (F5) in the IDE.
' 5. Sets the hyperlink to non-hyperlinked text.
' 6. Click the note in the drawing. Although the text in the note still
'    appears as http://www.solidworks.com, the note is no longer hyperlinked.
' 7. Close the Note PropertyManager page.
' 8. Examine the Immediate window.
'
' NOTES:
' * You cannot remove a hyperlink from a note
'   in a drawing using the user interface; you must use
'   the SOLIDWORKS API.
' * Because the drawing is used elsewhere, do not save changes.
'-------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swNote  As SldWorks.Note
    Dim swAnnotation As SldWorks.Annotation
    Dim swTextFormat As SldWorks.TextFormat
    Dim boolstatus As Boolean
    Dim longstatus As Long
    Dim longwarnings As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw", 3, 0, "", longstatus, longwarnings)
    Set swNote = swModel.InsertNote("http://www.solidworks.com")
    If Not swNote Is Nothing Then
       swNote.LockPosition = False
       swNote.Angle = 0
       boolstatus = swNote.SetBalloon(0, 0)
       Set swAnnotation = swNote.GetAnnotation()
       If Not swAnnotation Is Nothing Then
          longstatus = swAnnotation.SetLeader3(swLeaderStyle_e.swNO_LEADER, 0, True, False, False, False)
          boolstatus = swAnnotation.SetPosition(2.99923871594043E-02, 0.130309614693878, 0)
          boolstatus = swAnnotation.SetTextFormat(0, True, swTextFormat)
       End If
    End If
```

```
    Stop
    ' Click the note, close the SOLIDWORKS home web
    ' page, close the Note PropertyManager page,
    ' and click Continue (F5) in the IDE
```

```
    swModel.ClearSelection2 True
```

```
    swModel.WindowRedraw
```

```
    Debug.Print "Note = " & swNote.GetName
    Debug.Print "Tag name = " & swNote.TagName
    Debug.Print "Hyperlink  = " & swNote.GetHyperlinkText
    Debug.Print ""
```

```
    boolstatus = swNote.SetHyperlinkText("No longer a hyperlink")
    If boolstatus Then
        Debug.Print "Hyperlink set to non-hyperlinked text!"
    Else
        Debug.Print "Hyperlink not set to non-hyperlinked text!"
    End If
```

```
End Sub
```
