---
title: "Insert Magnetic Line Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Magnetic_Line_Example_VBNET.htm"
---

# Insert Magnetic Line Example (VB.NET)

This example shows how to insert a magnetic line in a drawing sheet.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\Assem20.slddrw.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:  At each Stop statement, observe the Immediate window
 ' and drawing, then press F5:
 ' 1. Inserts a magnetic line.
 ' 2. Attaches two notes to the magnetic line.
 ' 3. Detaches one note from the magnetic line.
 '
 ' NOTE: Because the drawing is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim swDraw As DrawingDoc
     Dim swNote As Note
     Dim anno As Annotation
     Dim MathUtil As MathUtility
     Dim StartPoint As MathPoint
     Dim EndPoint As MathPoint
     Dim NewLocation As MathPoint
     Dim MagLine As MagneticLine
     Dim startPointArray As Object
     Dim startPointCoords(2) As Double
     Dim endPointArray As Object
     Dim endPointCoords(2) As Double
     Dim vAnnPos As Object
     Dim myDrawingSheet As Sheet
     Dim boolstatus As Boolean
     Dim swSelMgr As SelectionMgr

     Sub main()

         Part = swApp.ActiveDoc
         swDraw = Part
         swSelMgr = Part.SelectionManager

         boolstatus = Part.Extension.SelectByID2("DetailItem350@Drawing View1",  "NOTE", 0.1999417828571, 0.1868875085714, 0, False, 0, Nothing, 0)
         swNote = swSelMgr.GetSelectedObject6(1, 0)

         MathUtil = swApp.GetMathUtility()

         startPointCoords(0) = 0.00792759673091
         startPointCoords(1) = 0.01114535920683
         startPointCoords(2) = 0
         startPointArray = startPointCoords
         StartPoint = MathUtil.CreatePoint((startPointArray))

         endPointCoords(0) = 0.2681801120698
         endPointCoords(1) = 0.2077950154354
         endPointCoords(2) = 0
         endPointArray = endPointCoords
         EndPoint = MathUtil.CreatePoint((endPointArray))

         myDrawingSheet = Part.GetCurrentSheet()
         Stop

         MagLine = myDrawingSheet.InsertMagneticLine(StartPoint, EndPoint)
         MagLine.EqualSpacing = True
         Debug.Print("Number of magnetic lines on this sheet: " & myDrawingSheet.GetMagneticLinesCount)
         Stop

         Debug.Print("First note attached to magnetic line? " & MagLine.AddNote(swNote, 0.000001))    ' If EqualSpacing is True then Position is ignored
         Debug.Print("Number of notes attached to the magnetic line: " & MagLine.GetNotesCount)
         Stop

         Debug.Print("Angle in radians of the magnetic line: " & MagLine.Angle)
         Debug.Print("Length in meters of the magnetic line: " & MagLine.Length)

         boolstatus = Part.Extension.SelectByID2("DetailItem352@Drawing View3",  "NOTE", 0.1944023085714, 0.1194905714286, 0, False, 0, Nothing, 0)
         swNote = swSelMgr.GetSelectedObject6(1, 0)
         Debug.Print("Second note attached to magnetic line? " & MagLine.AddNote(swNote, 0.000001))  ' This fails because note belongs to a different view
         anno = swNote.GetAnnotation
         Debug.Print("Number of notes attached to the magnetic line: " & MagLine.GetNotesCount)
         Stop

         boolstatus = Part.Extension.SelectByID2("DetailItem351@Drawing View1",  "NOTE", 0.1944023085714, 0.1194905714286, 0, False, 0, Nothing, 0)
         swNote = swSelMgr.GetSelectedObject6(1, 0)
         anno = swNote.GetAnnotation
         vAnnPos = anno.GetPosition
         Debug.Print("Second note attached to magnetic line? " & MagLine.AddNote(swNote, 0.000001))  ' This succeeds because note belongs to same view as previously added note
         Debug.Print("Number of notes attached to the magnetic line: " & MagLine.GetNotesCount)
         Stop

         ' Detach a note from the magnetic line
         NewLocation = MathUtil.CreatePoint((vAnnPos))
         Debug.Print("Note detached from magnetic line? " & MagLine.RemoveNote(swNote, NewLocation))  ' Move the note to its original position
         Debug.Print("Number of notes attached to the magnetic line: " & MagLine.GetNotesCount)

     End Sub

     Public swApp As SldWorks

 End  Class
```
