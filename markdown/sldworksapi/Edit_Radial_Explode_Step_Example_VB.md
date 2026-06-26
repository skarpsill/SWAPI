---
title: "Edit Radial Explode Step Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Radial_Explode_Step_Example_VB.htm"
---

# Edit Radial Explode Step Example (VBA)

This example shows how to edit a radial explode step in an explode view.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open  public_documents\samples\tutorial\api\RadialExplodeStep.sldasm.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates and explode view and gets the first explode step.
 ' 2. Gets the components to move.
 ' 3. Prints the current properties of the explode step.
 ' 4. Modifies the explode step properties.
 ' 5. Re-sets the components to move.
 ' 6. Re-sets the explode and diverge direction entities.
 ' 7. Inspect the Immediate window and the graphics area.
 '
 ' Note: Because the model is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.AssemblyDoc
 Dim swMdl As SldWorks.ModelDoc2
 Dim explStep As SldWorks.ExplodeStep
 Dim config As SldWorks.Configuration
 Dim comp As SldWorks.Component2
 Dim var As Variant
 Dim i As Long
 Dim transDir As SldWorks.Feature
 Dim divergeDir As SldWorks.Feature
 Dim num As Double
 Dim selComp(2) As SldWorks.Component2
 Dim sel3 As SldWorks.Feature
 Dim sel4 As SldWorks.Feature
 Dim transDir1 As SldWorks.Edge
 Dim divergeDir1 As SldWorks.Feature
 Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set config = swModel.ConfigurationManager.ActiveConfiguration
     Set swMdl = swModel

     Call swModel.AutoExplode

     Set explStep = config.GetExplodeStep(0)

    Debug.Print "Pre-Modification"
     Debug.Print ""

    var = explStep.GetComponents()
     Debug.Print "Components to move:"
     For i = 0 To UBound(var)
         Set comp = var(i)
         Debug.Print "  " & comp.Name2
     Next

    Debug.Print "Diverge from axis? " & explStep.DivergeFromAxis
     Debug.Print "Explode step: " & explStep.Name
     Debug.Print "Explode distance (m): " & explStep.ExplodeDistance
     Debug.Print "Explode step type as defined in swAssemblyExplodeStepType_e: " & explStep.ExplodeStepType
     Debug.Print "Rotation angle (rad): " & explStep.RotationAngle
     Debug.Print "Reverse rotation direction? " & explStep.ReverseRotationDirection
     Debug.Print "Reverse translation direction? " & explStep.ReverseTranslationDirection
     Debug.Print "Rotate about each component's origin? " & explStep.RotateAboutEachComponentOrigin

     Set divergeDir = explStep.DivergeDirection

    swMdl.ClearSelection2 (True)

    num = 3.1415 / 4

    explStep.DivergeFromAxis = Not explStep.DivergeFromAxis
     explStep.ExplodeDistance = 0.2
     explStep.RotationAngle = num
     explStep.ReverseRotationDirection = Not explStep.ReverseRotationDirection
     explStep.ReverseTranslationDirection = Not explStep.ReverseTranslationDirection
     explStep.RotateAboutEachComponentOrigin = Not explStep.RotateAboutEachComponentOrigin

    swMdl.ClearSelection2 (True)

    boolstatus = swMdl.Extension.SelectByID2("Part2-1@RadialExplodeStep", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
     boolstatus = swMdl.Extension.SelectByID2("Part2-2@RadialExplodeStep", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
     boolstatus = swMdl.Extension.SelectByID2("Part2-3@RadialExplodeStep", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)

    Set selComp(0) = swMdl.SelectionManager.GetSelectedObject6(1, -1)
     Set selComp(1) = swMdl.SelectionManager.GetSelectedObject6(2, -1)
     Set selComp(2) = swMdl.SelectionManager.GetSelectedObject6(3, -1)

    Call explStep.SetComponents(selComp)

    boolstatus = swMdl.Extension.SelectByID2("Axis5", "AXIS", 0, 0, 0, True, 2 + 32, Nothing, 0) ' Explode direction entity
     boolstatus = swMdl.Extension.SelectByID2("Axis4", "AXIS", 0, 0, 0, True, 64, Nothing, 0) ' Diverge direction entity

    Set sel3 = swMdl.SelectionManager.GetSelectedObject6(1, -1)
     Set sel4 = swMdl.SelectionManager.GetSelectedObject6(2, -1)

    explStep.SetExplodeDirection sel3, -1
     explStep.DivergeDirection = sel4

    Debug.Print ""
     Debug.Print "Post-Modification"
     Debug.Print ""

    var = explStep.GetComponents()
     Debug.Print "Components to move:"
     For i = 0 To UBound(var)
         Set comp = var(i)
         Debug.Print "  " & comp.Name2
     Next

    Debug.Print "Diverge from axis? " & explStep.DivergeFromAxis
     Debug.Print "Explode step: " & explStep.Name
     Debug.Print "Explode distance (m): " & explStep.ExplodeDistance
     Debug.Print "Explode step type as defined in swAssemblyExplodeStepType_e: " & explStep.ExplodeStepType
     Debug.Print "Rotation angle (rad): " & explStep.RotationAngle
     Debug.Print "Reverse rotation direction? " & explStep.ReverseRotationDirection
     Debug.Print "Reverse translation direction? " & explStep.ReverseTranslationDirection
     Debug.Print "Rotate about each component's origin? " & explStep.RotateAboutEachComponentOrigin

     Set divergeDir = explStep.DivergeDirection
End Sub
```
