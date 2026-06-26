---
title: "Attach Annotation Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Attach_Annotation_Example_CSharp.htm"
---

# Attach Annotation Example (C#)

This example shows how to attach an existing annotation to a drawing view.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\replaceview.slddrw.
 //
 // Postconditions:
 // 1. Inserts a note annotation n the drawing.
 // 2. Selects the annotation.
 // 3. Appends a face in a drawing view to the selection list.
 // 4. Attaches the annotation to the selected face.
 // 5. Examine the drawing.
 // 6. Close the drawing without saving it.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace AttachAnnotation_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 part;
         DrawingDoc draw;
         Note aNote;
         Annotation anAnnot;
         SelectData selectData = null;
         int ret;

         bool boolstatus;

         public void Main()
         {
             part = (ModelDoc2)swApp.ActiveDoc;
             draw = (DrawingDoc)part;

             boolstatus = draw.ActivateSheet("Sheet1");

             aNote = (Note)draw.CreateText2("This is a note.", 0.21, 0.12, 0, 0.005, 0);
             anAnnot = (Annotation)aNote.GetAnnotation();
             ret = anAnnot.SetLeader3(swLeaderStyle_e.swBENT, swLeaderSide_e.swLS_SMART,  true,  false,  false,  false);

             anAnnot.Select3(false, selectData);
             boolstatus = draw.ActivateView("Drawing View1");
             boolstatus = part.Extension.SelectByID2("", "FACE", 0.0783563575357558, 0.17448024010205, -499.965138294658,  true, 0,  null, 0);

             draw.AttachAnnotation(swAttachAnnotationOption_e.swAttachAnnotationOption_View);

         }

         public SldWorks swApp;

     }

 }
```
