---
title: "Copy and Paste Appearances Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Appearances_Example_VBNET.htm"
---

# Copy and Paste Appearances Example (VB.NET)

This example shows how to copy an appearance from one entity and apply it to other entities.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\introsw\vanity_assembly.sldasm.
 ' 2. Press F5 repeatedly while observing the changes in the appearances of
 '    entities in the model.
 '
 ' Postconditions: None
 '
 ' Note: Because the model is used elsewhere, do not save changes when closing.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc

         Dim pEnt As Object
         Dim selMgr As SelectionMgr
         selMgr = Part.SelectionManager

         Debug.Print("Selected a face, feature, body, component, or part and copied its appearance to the clipboard.")
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.196625056591301, -0.204766940654167, 0.863250195790926,  False, 0,  Nothing, 0)
         pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.CopyAppearance(pEnt)

         Debug.Print("Selected a face to which was applied the copied appearance.")
         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.273402696806954, 0.0150637315567224, 0.26416741603316,  False, 0,  Nothing, 0)
         pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetType_e.swAppearanceTargetFace)
         Stop

         Debug.Print("Selected a face to whose component was applied the copied appearance.")
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0259512148343788, 0.178648261563922, 1.13882797742889,  False, 0,  Nothing, 0)
         pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetType_e.swAppearanceTargetComponent)
         Stop

         Debug.Print("Selected a face to whose feature was applied the copied appearance.")
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.00438233207216854, 0.239755098177056, 0.383214316118654,  False, 0,  Nothing, 0)
         pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetType_e.swAppearanceTargetFeature)
         Stop

         Debug.Print("Selected a face to whose part was applied the copied appearance.")
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0112719408850239, 0.0695930730344685, 0.505696689751943,  False, 0,  Nothing, 0)
         pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetType_e.swAppearanceTargetPart)
         Stop

         Debug.Print("Selected a component to which was applied the copied appearance.")
         boolstatus = Part.Extension.SelectByID2("door-1@vanity_assembly", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         pEnt = selMgr.GetSelectedObject6(1, -1)
         'The second parameter of SldWorks::PasteAppearance is ignored, if the selected object is not a face.
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetType_e.swAppearanceTargetAppearanceFilter)
         Stop

     End Sub

     Public swApp As SldWorks

 End  Class
```
