---
title: "Detect Interferences Using a Transform Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Detect_Interferences_Using_a_Transform_Example_VB.htm"
---

# Detect Interferences Using a Transform Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim swDoc As SldWorks.ModelDoc2
 Dim swADoc As SldWorks.AssemblyDoc
 Dim swSM As SldWorks.SelectionMgr
 Dim swIDM As InterferenceDetectionMgr
 Dim swComp() As SldWorks.Component2
 Dim varComp As Variant
 Dim numOfComp As Long
 Dim swCompTrans() As SldWorks.MathTransform
 Dim varCompTrans As Variant
 Dim isInterfering As Boolean
 Dim outIntComp As Variant
 Dim outIntFaces As Variant
 Dim gposX As Double
 Dim gposY As Double
 Dim I As Long
Option Explicit
' Uncomment one of the following lines to transform the components
     'Const userOpt = 0 'make components coincident
     Const userOpt = 1 'make components intersecting
Sub main()

    Set swApp = Application.SldWorks
     Set swDoc = swApp.ActiveDoc
     Set swADoc = swDoc
     Set swSM = swDoc.SelectionManager
     SetPosAsPerOption
     SelectAllComponent
     isInterfering = False
     numOfComp = swSM.GetSelectedObjectCount
     If (numOfComp) Then

        getSelectedComp
         PrintComponentName varComp
         CreateSameTransMatAsCompCount
         ChangePosOfCompAsPerOption

        varCompTrans = swCompTrans

        Set swIDM = swADoc.InterferenceDetectionManager
         swIDM.TreatCoincidenceAsInterference = True
         isInterfering = swIDM.GetComponentsTransformInterference((varComp), (varCompTrans), outIntComp)

        Stop ' Observe transformation of objects for interference detection

        swIDM.Done ' Interference detection stopped
         PrintInterferenceInfo
         varComp = Empty
     Else
         MsgBox ("Select components")
     End If
End Sub
 Sub SetPosAsPerOption()
     If (userOpt = 0) Then
         gposX = 100 / 1000
         gposY = -50 / 1000
     ElseIf (userOpt = 1) Then
         gposX = 70 / 1000
         gposY = -50 / 1000
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
         Debug.Print ("Interfering components:")
         Debug.Print ("")
         For I = 0 To UBound(outIntComp)
             Dim swOutComp As SldWorks.Component2
             Set swOutComp = outIntComp(I)
             Debug.Print (swOutComp.Name2)
             swOutComp.Select4 True, Nothing, False
             Set swOutComp = Nothing
         Next I
     Else
         Debug.Print ("No interference")
     End If
 End Sub
 Sub getSelectedComp()
     ReDim swComp(numOfComp - 1)
     For I = 1 To numOfComp
         Set swComp(I - 1) = swSM.GetSelectedObject6(I, -1)
     Next I
     varComp = swComp
 End Sub
 Sub PrintComponentName(varComp As Variant)
     If Not (IsEmpty(varComp)) Then
         If userOpt = 0 Then
             Debug.Print ("Detect interferences between coincident components:")
             Debug.Print ("")
         Else
             Debug.Print ("Detect interferences between intersecting components:")
             Debug.Print ("")
         End If

         For I = LBound(varComp) To UBound(varComp)
             Dim swComp As SldWorks.Component2
             Set swComp = varComp(I)

            Debug.Print ("Component name : " & swComp.Name2)
             Set swComp = Nothing
         Next I
     End If
     Debug.Print ("")
 End Sub
 Sub CreateSameTransMatAsCompCount()
     ReDim swCompTrans(numOfComp - 1)
     If Not (IsEmpty(varComp)) Then
         For I = LBound(varComp) To UBound(varComp)
             Dim swComp As SldWorks.Component2
             Set swComp = varComp(I)
             Set swCompTrans(I) = swComp.Transform2
             Set swComp = Nothing
         Next I
     End If
 End Sub
 Sub ChangePosOfCompAsPerOption()
     ChangeRefPosOfComp gposX, gposY
 End Sub
Sub ChangePosOfComp(compNum As Long, pos As Double)
     Dim varData As Variant
     varData = swCompTrans(compNum).ArrayData
     varData(9) = pos
     swCompTrans(compNum).ArrayData = varData
 End Sub
Sub ChangeRefPosOfComp(posX As Double, posY As Double)
     If Not (IsEmpty(varComp)) Then
         For I = LBound(varComp) To UBound(varComp)
             If (I > 0) Then
                 Dim varData As Variant
                 varData = swCompTrans(I).ArrayData
                 varData(9) = posX * I
                 varData(10) = posY * I
                 swCompTrans(I).ArrayData = varData
                 If (userOpt = 2) Then
                     swComp(I).Transform2 = swCompTrans(I)
                     swDoc.ForceRebuild3 True
                 End If
             End If
         Next I
     End If
 End Sub
```
