---
title: "Insert Magnetic Line Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Magnetic_Line_Example_CSharp.htm"
---

# Insert Magnetic Line Example (C#)

This example shows how to insert a magnetic line in a drawing sheet.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\Assem20.slddrw.
 // 2. Open the Immediate window.
 //
 // Postconditions: At each   System.Diagnostics.Debugger.Break() statement,
 // observe the Immediate window and drawing, then press F5:
 // 1. Inserts a magnetic line.
 // 2. Attaches two notes to the magnetic line.
 // 3. Detaches one note from the magnetic line.
 //
 // NOTE: Because the drawing is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertMagneticLine_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         DrawingDoc swDraw;
         Note swNote;
         Annotation anno;
         MathUtility MathUtil;
         MathPoint StartPoint;
         MathPoint EndPoint;
         MathPoint NewLocation;
         MagneticLine MagLine;
         object startPointArray;
         double[] startPointCoords = new double[3];
         object endPointArray;
         double[] endPointCoords = new double[3];
         object vAnnPos;
         Sheet myDrawingSheet;
         bool boolstatus;

         SelectionMgr swSelMgr;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)Part;
             swSelMgr = (SelectionMgr)Part.SelectionManager;

             boolstatus = Part.Extension.SelectByID2("DetailItem350@Drawing View1",  "NOTE", 0.1999417828571, 0.1868875085714, 0, false, 0, null, 0);
             swNote = (Note)swSelMgr.GetSelectedObject6(1, 0);

             MathUtil = (MathUtility)swApp.GetMathUtility();

             startPointCoords[0] = 0.00792759673091;
             startPointCoords[1] = 0.01114535920683;
             startPointCoords[2] = 0;
             startPointArray = startPointCoords;
             StartPoint = (MathPoint)MathUtil.CreatePoint((startPointArray));

             endPointCoords[0] = 0.2681801120698;
             endPointCoords[1] = 0.2077950154354;
             endPointCoords[2] = 0;
             endPointArray = endPointCoords;
             EndPoint = (MathPoint)MathUtil.CreatePoint((endPointArray));

             myDrawingSheet = (Sheet)swDraw.GetCurrentSheet();
             System.Diagnostics.Debugger.Break();

             MagLine = myDrawingSheet.InsertMagneticLine(StartPoint, EndPoint);
             MagLine.EqualSpacing =  true;
             Debug.Print("Number of magnetic lines on this sheet: " + myDrawingSheet.GetMagneticLinesCount());
             System.Diagnostics.Debugger.Break();

             Debug.Print("First note attached to magnetic line? " + MagLine.AddNote(swNote, 1E-06));
             // If EqualSpacing is True then Position is ignored
             Debug.Print("Number of notes attached to the magnetic line: " + MagLine.GetNotesCount());
             System.Diagnostics.Debugger.Break();

             Debug.Print("Angle in radians of the magnetic line: " + MagLine.Angle);
             Debug.Print("Length in meters of the magnetic line: " + MagLine.Length);

             boolstatus = Part.Extension.SelectByID2("DetailItem352@Drawing View3",  "NOTE", 0.1944023085714, 0.1194905714286, 0, false, 0, null, 0);
             swNote = (Note)swSelMgr.GetSelectedObject6(1, 0);
             Debug.Print("Second note attached to magnetic line? " + MagLine.AddNote(swNote, 1E-06));
             // This fails because note belongs to a different view
             anno = (Annotation)swNote.GetAnnotation();
             Debug.Print("Number of notes attached to the magnetic line: " + MagLine.GetNotesCount());
             System.Diagnostics.Debugger.Break();

             boolstatus = Part.Extension.SelectByID2("DetailItem351@Drawing View1",  "NOTE", 0.1944023085714, 0.1194905714286, 0, false, 0, null, 0);
             swNote = (Note)swSelMgr.GetSelectedObject6(1, 0);
             anno = (Annotation)swNote.GetAnnotation();
             vAnnPos = anno.GetPosition();
             Debug.Print("Second note attached to magnetic line? " + MagLine.AddNote(swNote, 1E-06));
             // This succeeds because note belongs to same view as previously added note
             Debug.Print("Number of notes attached to the magnetic line: " + MagLine.GetNotesCount());
             System.Diagnostics.Debugger.Break();

             // Detach a note from the magnetic line
             NewLocation = (MathPoint)MathUtil.CreatePoint((vAnnPos));
             Debug.Print("Note detached from magnetic line? " + MagLine.RemoveNote(swNote, NewLocation));
             // Move the note to its original position
             Debug.Print("Number of notes attached to the magnetic line: " + MagLine.GetNotesCount());

         }

         public SldWorks swApp;

     }

 }
```
