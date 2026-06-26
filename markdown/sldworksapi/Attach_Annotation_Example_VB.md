---
title: "Attach Annotation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Attach_Annotation_Example_VB.htm"
---

# Attach Annotation Example (VBA)

This example shows how to attach an existing annotation to a drawing view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\replaceview.slddrw.
 '
 ' Postconditions:
 ' 1. Inserts a note annotation in the drawing.
 ' 2. Selects the annotation.
 ' 3. Appends a face in a drawing view to the selection list.
 ' 4. Attaches the annotation to the selected face.
 ' 5. Examine the drawing.
 ' 6. Close the drawing without saving it.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim part As SldWorks.ModelDoc2
 Dim draw As SldWorks.DrawingDoc
 Dim aNote As SldWorks.Note
 Dim anAnnot As SldWorks.Annotation
 Dim selectData As SldWorks.selectData
 Dim ret As Long
 Dim boolstatus As Boolean
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set part = swApp.ActiveDoc
     Set draw = part

    boolstatus = part.ActivateSheet("Sheet1")

    Set aNote = draw.CreateText2("This is a note.", 0.21, 0.12, 0, 0.005, 0)
     Set anAnnot = aNote.GetAnnotation
     ret = anAnnot.SetLeader3(swLeaderStyle_e.swBENT, swLeaderSide_e.swLS_SMART, True, False, False, False)

    anAnnot.Select3 False, selectData
     boolstatus = part.ActivateView("Drawing View1")
     boolstatus = part.Extension.SelectByID2("", "FACE", 7.83563575357558E-02, 0.17448024010205, -499.965138294658, True, 0, Nothing, 0)

    draw.AttachAnnotation swAttachAnnotationOption_e.swAttachAnnotationOption_View
End Sub
```
