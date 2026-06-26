---
title: "Detect Interferences Using a Transform Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Detect_Interferences_Using_a_Transform_Example_VBNET.htm"
---

# Detect Interferences Using a Transform Example (VB.NET)

This example shows how to specify a transform to detect interferences.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\InterferenceAssem.sldasm.
 ' 2. Uncomment one of the userOpt assignments.
 '
 ' Postconditions:
 ' 1. When the macro stops, observe the position of the components in the
 '    graphics area.
 ' 2. Press F5 to continue.
 ' 3. Inspect the Immediate Window for interfering components.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDoc As ModelDoc2
     Dim swADoc As AssemblyDoc
     Dim swSM As SelectionMgr
     Dim swIDM As InterferenceDetectionMgr
     Dim swComp() As Component2
     Dim varComp As Object
     Dim numOfComp As Long
     Dim swCompTrans() As MathTransform
     Dim varCompTrans As Object
     Dim isInterfering As Boolean
     Dim outIntComp As Object
     Dim outIntFaces As Object
     Dim gposX As Double
     Dim gposY As Double
     Dim I As  Long

     ' Uncomment one of the following lines to transform the components
     'Dim userOpt As Long = 0 'make components coincident
     Dim userOpt As Long = 1 'make components intersecting

     Sub main()

         swDoc = swApp.ActiveDoc
         swADoc = swDoc
         swSM = swDoc.SelectionManager
         SetPosAsPerOption()
         SelectAllComponent()
         isInterfering = False
         numOfComp = swSM.GetSelectedObjectCount
         If (numOfComp) Then

             getSelectedComp()
             PrintComponentName(varComp)
             CreateSameTransMatAsCompCount()
             ChangePosOfCompAsPerOption()

             varCompTrans = swCompTrans

             swIDM = swADoc.InterferenceDetectionManager
             swIDM.TreatCoincidenceAsInterference =  True
             isInterfering = swIDM.GetComponentsTransformInterference((varComp), (varCompTrans), outIntComp)

             Stop ' Observe transformation of objects for interference detection

             swIDM.Done()  ' Interference detection stopped
             PrintInterferenceInfo()
             varComp = Nothing
         Else
             MsgBox("Select components")
         End If

     End Sub
     Sub SetPosAsPerOption()
         If (userOpt = 0) Then
             gposX = 100.0 / 1000.0
             gposY = -50.0 / 1000.0
         ElseIf (userOpt = 1) Then
             gposX = 70.0 / 1000.0
             gposY = -50.0 / 1000.0
         End If
     End Sub
     Sub SelectAllComponent()
         Dim boolstatus As Boolean
         boolstatus = swDoc.Extension.SelectByID2("SquarePad_Red-1@InterferenceAssem", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         boolstatus = swDoc.Extension.SelectByID2("SquarePad_Green-1@InterferenceAssem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = swDoc.Extension.SelectByID2("SquarePad_Blue-1@InterferenceAssem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = swDoc.Extension.SelectByID2("SquarePad_Orange-1@InterferenceAssem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = swDoc.Extension.SelectByID2("SquarePad_SkyBlue-1@InterferenceAssem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = swDoc.Extension.SelectByID2("SquarePad_Yellow-1@InterferenceAssem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
         boolstatus = swDoc.Extension.SelectByID2("SquarePad_Pink-1@InterferenceAssem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
     End Sub
     Sub PrintInterferenceInfo()
         If (isInterfering) Then
             Debug.Print("Interfering components:")
             Debug.Print("")
             For I = 0 To UBound(outIntComp)
                 Dim swOutComp As Component2
                 swOutComp = outIntComp(I)
                 Debug.Print(swOutComp.Name2)
                 swOutComp.Select4(True, Nothing, False)
                 swOutComp = Nothing
             Next I
         Else
             Debug.Print("No interference")
         End If
     End Sub
     Sub getSelectedComp()
         ReDim swComp(numOfComp - 1)
         For I = 1 To numOfComp
             swComp(I - 1) = swSM.GetSelectedObject6(I, -1)
         Next I
         varComp = swComp
     End Sub
     Sub PrintComponentName(ByVal varComp As Object)
         If Not (IsNothing(varComp)) Then
             If userOpt = 0 Then
                 Debug.Print("Detect interferences between coincident components:")
                 Debug.Print("")
             Else
                 Debug.Print("Detect interferences between intersecting components:")
                 Debug.Print("")
             End If

             For I = LBound(varComp) To UBound(varComp)
                 Dim swComp As Component2
                 swComp = varComp(I)

                 Debug.Print("Component name : " & swComp.Name2)
                 swComp = Nothing
             Next I
         End If
         Debug.Print("")
     End Sub
     Sub CreateSameTransMatAsCompCount()
         ReDim swCompTrans(numOfComp - 1)
         If Not (IsNothing(varComp)) Then
             For I = LBound(varComp) To UBound(varComp)
                 Dim swComp As Component2
                 swComp = varComp(I)
                 swCompTrans(I) = swComp.Transform2
                 swComp = Nothing
             Next I
         End If
     End Sub
     Sub ChangePosOfCompAsPerOption()
         ChangeRefPosOfComp(gposX, gposY)
     End Sub

     Sub ChangeRefPosOfComp(ByVal posX As Double, ByVal posY As  Double)
         If Not (IsNothing(varComp)) Then
             For I = LBound(varComp) To UBound(varComp)
                 If (I > 0) Then
                     Dim varData As Object
                     varData = swCompTrans(I).ArrayData
                     varData(9) = posX * I
                     varData(10) = posY * I
                     swCompTrans(I).ArrayData = varData
                     If (userOpt = 2) Then
                         swComp(I).Transform2 = swCompTrans(I)
                         swDoc.ForceRebuild3(True)
                     End If
                 End If
             Next I
         End If
     End Sub

     Public swApp As SldWorks

 End  Class
```
