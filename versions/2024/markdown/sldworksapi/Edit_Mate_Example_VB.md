---
title: "Edit Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Mate_Example_VB.htm"
---

# Edit Mate Example (VBA)

This example shows how to edit an assembly mate.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly with a mate.
 ' 2. Select a mate.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Edits the selected assembly mate.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Modifying a mate can cause mate errors.
 '----------------------------------------------------------------------------
Option Explicit
Function SelectMateEntity(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swMateEnt As SldWorks.MateEntity2, nMark As Long) As Boolean
    Dim swEnt As SldWorks.Entity
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim swSelData As SldWorks.SelectData
     Dim bRet As Boolean
    Select Case swMateEnt.ReferenceType
        Case swMateEntity2ReferenceType_Point, _
                 swMateEntity2ReferenceType_Line, _
                 swMateEntity2ReferenceType_Circle, _
                 swMateEntity2ReferenceType_Plane, _
                 swMateEntity2ReferenceType_Cylinder, _
                 swMateEntity2ReferenceType_Sphere, _
                 swMateEntity2ReferenceType_Cone, _
                 swMateEntity2ReferenceType_SweptSurface
            Set swSelMgr = swModel.SelectionManager
             Set swSelData = swSelMgr.CreateSelectData
             Set swEnt = swMateEnt.Reference
            swSelData.Mark = nMark
            bRet = swEnt.Select4(True, swSelData)
            SelectMateEntity = bRet
            Exit Function
        Case swMateEntity2ReferenceType_Set, _
                 swMateEntity2ReferenceType_MultipleSurface, _
                 swMateEntity2ReferenceType_GenSurface, _
                 swMateEntity2ReferenceType_Ellipse, _
                 swMateEntity2ReferenceType_GeneralCurve, _
                 swMateEntity2ReferenceType_UNKNOWN
        Case Else
    End Select
    SelectMateEntity = False
End Function
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swAssy As SldWorks.AssemblyDoc
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim swFeat As SldWorks.Feature
     Dim swMate As SldWorks.Mate2
     Dim swDispDim As SldWorks.DisplayDimension
     Dim swDim As SldWorks.Dimension
     Dim sVarType As String
     Dim nVarFactor As Double
     Dim nMateDist As Double
     Dim nNumMateEnt As Long
     Dim swMateEnt() As SldWorks.MateEntity2
     Dim vMateEntPar As Variant
     Dim swComp As SldWorks.Component2
     Dim nNewMateAlign As Long
     Dim nRetVal As Long
     Dim i As Long
     Dim bRet As Boolean
     Dim vDimValueArr As Variant
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssy = swModel
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swMate = swFeat.GetSpecificFeature2
     Set swDispDim = swMate.DisplayDimension2(0)
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swFeat.Name
     Debug.Print "    Type           = " & swMate.Type
     Debug.Print "    Alignment      = " & swMate.Alignment
     Debug.Print "    CanBeFlipped   = " & swMate.CanBeFlipped
    Select Case swMate.Type
        Case swMateANGLE
            sVarType = " deg"
             ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
             nVarFactor = 57.3
        Case swMateDISTANCE
            sVarType = " mm"
             nVarFactor = 1000#
        Case swMateGEAR
            sVarType = " ratio"
             nVarFactor = 1#
    End Select
    If swMateANGLE = swMate.Type Or swMateDISTANCE = swMate.Type Then
        Debug.Print "    MaxVar         = " & swMate.MaximumVariation * nVarFactor & sVarType
         Debug.Print "    MinVar         = " & swMate.MinimumVariation * nVarFactor & sVarType
    End If
    If Not swDispDim Is Nothing Then
        Set swDim = swDispDim.GetDimension
        vDimValueArr = swDim.GetSystemValue3(swThisConfiguration, Empty)
        Debug.Print "    Dim Value      = " & vDimValueArr(0) * nVarFactor & sVarType
    End If
    nNumMateEnt = swMate.GetMateEntityCount
    ReDim swMateEnt(nNumMateEnt)
    For i = 0 To nNumMateEnt - 1
        Set swMateEnt(i) = swMate.MateEntity(i)
         Set swComp = swMateEnt(i).ReferenceComponent
        vMateEntPar = swMateEnt(i).EntityParams
        Debug.Print "      RefType(" & i & ")   = " & swMateEnt(i).ReferenceType
         Debug.Print "        Component          = " & swComp.Name2 & " (" & swComp.ReferencedConfiguration & ") --> " & swComp.GetPathName
         Debug.Print "        Point              = (" & vMateEntPar(0) * 1000# & ", " & vMateEntPar(1) * 1000# & ", " & vMateEntPar(2) * 1000# & ") mm"
         Debug.Print "        Vector             = (" & vMateEntPar(3) & ", " & vMateEntPar(4) & ", " & vMateEntPar(5) & ")"
         Debug.Print "        Radius 1           = " & vMateEntPar(6) * 1000# & " mm"
         Debug.Print "        Radius 2           = " & vMateEntPar(7) * 1000# & " mm"
    Next i
    Select Case swMate.Type
        Case swMateGEAR
             ' Cannot change alignment on these mate types
             Exit Sub
    End Select
    If swMateAlignALIGNED = swMate.Alignment Then
         nNewMateAlign = swMateAlignANTI_ALIGNED
     Else
        If swMateAlignANTI_ALIGNED = swMate.Alignment Then
             nNewMateAlign = swMateAlignALIGNED
        Else
            Exit Sub
        End If
    End If
    swModel.ClearSelection2 True
    For i = 0 To nNumMateEnt - 1
        '   IAssemblyDoc::EditMate3 requires that mate entities
         '   be selected with mark of 1 except for:
         '       swMateCAMFOLLOWER
         '           cam face              --> 1
         '           cam follower face     --> 8
         '       swMateSYMMETRIC
         '           symmetry faces        --> 1
         '           symmetry plane        --> 4
        bRet =  SelectMateEntity(swApp, swModel, swMateEnt(i), 1)
    Next i
    ' IAssemblyDoc::EditMate3 requires mate feature to be selected last
     ' Mark is ignored
     bRet = swFeat.Select2(True, 0)
    swAssy.EditMate3 _
         swMate.Type, _
         nNewMateAlign, _
         True, _
         nMateDist, _
         swMate.MaximumVariation, _
         swMate.MinimumVariation, _
         0#, _
         0#, _
         nMateDist, _
         swMate.MaximumVariation, _
         swMate.MinimumVariation, _
         False, _
         True, _
         0, _
         nRetVal
    bRet = swModel.EditRebuild3
End Sub
```
