---
title: "Change Text Format Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Text_Format_Example_VB.htm"
---

# Change Text Format Example (VBA)

This example shows how to change the text format of an annotation.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing that has at least
'    one annotation containing text.
' 2. Select that annotation.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Changes the text format of the selected annotation.
' 2. Examine the annotation in the graphics area and
'    the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swAnnObj                    As Object
    Dim swAnn                       As SldWorks.Annotation
    Dim swTextFormat                As SldWorks.TextFormat
    Dim i                           As Long
    Dim bRet                        As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swAnnObj = swSelMgr.GetSelectedObject6(1, -1)
    Set swAnn = swAnnObj.GetAnnotation
```

```
    'Get text format information
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swAnn.GetName & " <" & swAnn.GetType & ">"
```

```
    For i = 0 To swAnn.GetTextFormatCount - 1
        Set swTextFormat = swAnn.GetTextFormat(i)
```

```
        'Change text to be 10mm, bold, italic, and Comic Sans MS font
        swTextFormat.CharHeight = 0.01
        swTextFormat.Bold = True
        swTextFormat.Italic = True
        swTextFormat.TypeFaceName = "Comic Sans MS"
        bRet = swAnn.SetTextFormat(i, False, swTextFormat)
    Next
```

```
End Sub
```
