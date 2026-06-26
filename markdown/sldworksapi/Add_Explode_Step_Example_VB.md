---
title: "Add Explode Step Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Explode_Step_Example_VB.htm"
---

# Add Explode Step Example (VBA)

## Add Regular Explode Step Example (VBA)

This example shows how to add a regular (translate and rotate) explode step to an explode view.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open  public_documents\samples\tutorial\api\RegularExplodeStep.sldasm.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates an explode view.
 ' 2. Deletes the first explode step.
 ' 3. Adds a regular explode step.
 ' 4. Inspect the Immediate window and the graphics area.
 '
 ' Note: Because the model is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.AssemblyDoc
 Dim config As SldWorks.Configuration
 Dim swMdl As SldWorks.ModelDoc2
 Dim explStep As SldWorks.ExplodeStep
 Dim num As Double
 Dim comp As SldWorks.Component2
 Dim var As Variant
 Dim transDir As SldWorks.Edge
 Dim angleDir As SldWorks.Feature
 Dim obj As SldWorks.Component2
 Dim steps As Variant
 Dim nestedStep As SldWorks.ExplodeStep
 Dim boolstatus As Boolean
 Dim i As Long, j As Long
 Dim errCode As Long

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set config = swModel.ConfigurationManager.ActiveConfiguration
     Set swMdl = swModel

    Call swModel.AutoExplode

    Set explStep = config.GetExplodeStep(0)

    'If the first step is a subassembly explode step, get the nested explode steps
     If explStep.ExplodeStepType = swAssemblyExplodeStepType_SubAssembly Then
            Debug.Print "  Subassembly explode step" & explStep.Name
            steps = explStep.GetSubAssemblyExplodeSteps()

            For j = 0 To UBound(steps)
                 Set nestedStep = steps(j)
                Debug.Print "    Name: " & nestedStep.Name
                 Debug.Print "    Explode distance: " & nestedStep.ExplodeDistance
                 Debug.Print "    Explode rotation angle:  " & nestedStep.RotationAngle
            Next
     End If
    config.DeleteExplodeStep (explStep.Name)

     'Select the components to move
    boolstatus = swModel.Extension.SelectByID2("Testimo1-2@RegularExplodeStep", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
     boolstatus = swModel.Extension.SelectByID2("Testimo1-3@RegularExplodeStep", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
     boolstatus = swModel.Extension.SelectByID2("Testimo1-4@RegularExplodeStep", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)

    'Select the axis of explode direction
     boolstatus = swModel.Extension.SelectByRay(9.95048714770577E-02, 0.104317306113359, 5.68280010933222E-02, -2.53410890435057E-03, -0.389900775392565, 0.920853388786911, 6.25890574839405E-03, 1, True, 2, 0)

    num = 3.1415 / 3
     Set explStep = config.AddExplodeStep2(0.5, -1, True, num, -1, True, False, True, errCode)

    Call swMdl.EditRebuild3

    var = explStep.GetComponents()

    Debug.Print "Explode step: " & explStep.Name
     Debug.Print "Explode distance (m): " & explStep.ExplodeDistance
     Debug.Print "Explode step type as defined in swAssemblyExplodeStepType_e: " & explStep.ExplodeStepType
     Debug.Print "Rotation angle (rad): " & explStep.RotationAngle
     Debug.Print "Reverse rotation direction? " & explStep.ReverseRotationDirection
     Debug.Print "Reverse translation direction? " & explStep.ReverseTranslationDirection
     Debug.Print "Rotate about each component's origin? " & explStep.RotateAboutEachComponentOrigin
     Debug.Print "Automatically space components on drag? " & explStep.AutoSpaceComponentsOnDrag

      Debug.Print "Components to move:"
     For i = 0 To UBound(var)
         Set comp = var(i)
         Debug.Print "  " & comp.Name2
     Next

End Sub
```
