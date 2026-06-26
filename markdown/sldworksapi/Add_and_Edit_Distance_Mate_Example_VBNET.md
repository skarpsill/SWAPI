---
title: "Add and Edit Distance Mate Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Edit_Distance_Mate_Example_VBNET.htm"
---

# Add and Edit Distance Mate Example (VB.NET)

This example shows how to add and edit a cylindrical distance mate.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure the specified template exists.
 ' 2. Open public_documents\samples\tutorial\api\cylinder20.sldprt.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates and saves a new cylindrical part.
 ' 2. Adds two cylindrical entities to a new assembly.
  ' 3. Creates a distance mate between the cylindrical entities.
  ' 4. Edits the distance mate to change the distance from 0.2 to 0.3.
  ' 5. Inspect the Immediate window, the graphics area, and the Mates folder
 '    of the FeatureManager design tree.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swAssembly As AssemblyDoc
         Dim Part As ModelDoc2
         Dim AssemblyTitle As String
         Dim swInsertedComponent As Component2
         Dim swFeat As Feature
         Dim boolstatus As Boolean
         Dim longstatus As Integer, longwarnings As Integer
         Dim swSheetWidth As Double
         Dim swSheetHeight As Double
         Dim swMate As Mate2
         Dim tmpObj As ModelDoc2
         Dim errors As Integer
         Dim swEnt1 As Entity
         Dim swEnt2 As Entity

         Part = swApp.ActiveDoc

         ' Shell the active part
         boolstatus = Part.Extension.SelectByRay(-0.0108900020093756, 0.0655319999998483, -0.00515652172191494, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00167637314537445, 2, False, 1, 0)
         Part.InsertFeatureShell(0.00254, False)

         ' Save the shelled part
         longstatus = Part.SaveAs3("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 0, 2)

         ' Create a new assembly
         swSheetWidth = 0
         swSheetHeight = 0
         Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2018\templates\Assembly.asmdot", 0, swSheetWidth, swSheetHeight)

         ' Insert a cylinder20_shell component
         AssemblyTitle = Part.GetTitle
         tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 1, 32, "", longstatus, longwarnings)
         Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, longstatus)
         swInsertedComponent = Part.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 0, "", False, "", 0.119562469422817, -0.0102308109635487, -0.0474663286004215)
         swApp.CloseDoc("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt")

         ' Insert another cylinder20_shell component
         tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 1, 32, "", errors, longwarnings)
         Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)
         swInsertedComponent = Part.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt", 0, "", False, "", -0.130620346986689, -0.0101738580269739, 0.084551733918488)
         swApp.CloseDoc("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20_shell.sldprt")

         ' Select two cylindrical entities
         boolstatus = Part.Extension.SelectByRay(-0.140174514310559, 0.00237221117538411, 0.0264513806530431, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00086563679245283, 2, False, 1, 0)
         swEnt1 = Part.SelectionManager.GetSelectedObject6(1, -1)
         boolstatus = Part.Extension.SelectByRay(0.0679787981690652, -0.00725673614920197, -0.0758574895979791, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000636203082166533, 2, True, 1, 0)
         swEnt2 = Part.SelectionManager.GetSelectedObject6(1, -1)

         swEnt1.Select4(True, Nothing)
         swEnt2.Select4(True, Nothing)

         ' Add a center-to-center distance mate between the selected cylindrical entities
         swAssembly = Part
         swMate = swAssembly.AddDistanceMate(2, False, 0.2, 0, 0, 1, 1, errors)
         Debug.Print("First arc condition as defined in swDistanceMateArcConditions_e: " & swMate.DistanceFirstArcCondition)
         Debug.Print("Second arc condition as defined in swDistanceMateArcConditions_e: " & swMate.DistanceSecondArcCondition)
         swFeat = swMate

         Part.EditRebuild3

         ' Edit the distance mate to change the distance from 0.2 to 0.3
         boolstatus = Part.Extension.SelectByRay(-0.0936626010895907, 0.000678476678046991, -0.000454698905400619, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000808436123348018, 2, True, 1, 0)
         swEnt1 = Part.SelectionManager.GetSelectedObject6(1, -1)
         boolstatus = Part.Extension.SelectByRay(0.0803986691953469, -0.00107796570199525, -0.0914337018962783, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000808436123348018, 2, True, 2, 0)
         swEnt2 = Part.SelectionManager.GetSelectedObject6(2, -1)

         swEnt1.Select4(True, Nothing)
         swEnt2.Select4(True, Nothing)
         swFeat.Select2(True, 0)

         swAssembly.EditDistanceMate(2, False, 0.3, 0, 0, 1, 1, errors)

         Part.EditRebuild3

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
