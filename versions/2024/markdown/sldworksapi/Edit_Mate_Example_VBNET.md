---
title: "Edit Mate Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Mate_Example_VBNET.htm"
---

# Edit Mate Example (VB.NET)

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
 ' Note: Modifying a mate can cause mate errors.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Function SelectMateEntity(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swMateEnt As MateEntity2, ByVal nMark As Integer) As  Boolean

         Dim swEnt As Entity
         Dim swSelMgr As SelectionMgr
         Dim swSelData As SelectData
         Dim bRet As Boolean

         Select Case swMateEnt.ReferenceType

             Case swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Point, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Line, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Circle, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Plane, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Cylinder, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Sphere, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Cone, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_SweptSurface

                 swSelMgr = swModel.SelectionManager
                 swSelData = swSelMgr.CreateSelectData
                 swEnt = swMateEnt.Reference

                 swSelData.Mark = nMark

                 bRet = swEnt.Select4(True, swSelData)

                 SelectMateEntity = bRet

                 Exit Function

             Case swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Set, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_MultipleSurface, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_GenSurface, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_Ellipse, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_GeneralCurve, _
                     swMateEntity2ReferenceType_e.swMateEntity2ReferenceType_UNKNOWN

             Case Else

         End Select

         SelectMateEntity =  False

     End Function

     Sub main()

         Dim swModel As ModelDoc2
         Dim swAssy As AssemblyDoc
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swMate As Mate2
         Dim swDispDim As DisplayDimension
         Dim swDim As Dimension
         Dim sVarType As String = Nothing
         Dim nVarFactor As Double
         Dim nMateDist As Double
         Dim nNumMateEnt As Integer
         Dim swMateEnt() As MateEntity2
         Dim vMateEntPar As Object
         Dim swComp As Component2
         Dim nNewMateAlign As Integer
         Dim nRetVal As Integer
         Dim i As  Integer
         Dim bRet As Boolean
         Dim vDimValueArr As Object

         swModel = swApp.ActiveDoc
         swAssy = swModel
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swMate = swFeat.GetSpecificFeature2
         swDispDim = swMate.DisplayDimension2(0)

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    Type           = " & swMate.Type)
         Debug.Print("    Alignment      = " & swMate.Alignment)
         Debug.Print("    CanBeFlipped   = " & swMate.CanBeFlipped)

         Select Case swMate.Type

             Case swMateType_e.swMateANGLE

                 sVarType = " deg"
                 '  1 radian = 180º/p = 57.295779513º or approximately 57.3º
                 nVarFactor = 57.3

             Case swMateType_e.swMateDISTANCE

                 sVarType = " mm"
                 nVarFactor = 1000.0#

             Case swMateType_e.swMateGEAR

                 sVarType = " ratio"
                 nVarFactor = 1.0#

         End Select

         If swMateType_e.swMateANGLE = swMate.Type  Or swMateType_e.swMateDISTANCE = swMate.Type  Then

             Debug.Print("    MaxVar         = " & swMate.MaximumVariation * nVarFactor & sVarType)
             Debug.Print("    MinVar         = " & swMate.MinimumVariation * nVarFactor & sVarType)

         End If

         If Not swDispDim Is Nothing Then

             swDim = swDispDim.GetDimension
             vDimValueArr = swDim.GetSystemValue3(swInConfigurationOpts_e.swThisConfiguration, Nothing)
             Debug.Print("    Dim Value      = " & vDimValueArr(0) * nVarFactor & sVarType)

         End If

         nNumMateEnt = swMate.GetMateEntityCount

         ReDim swMateEnt(nNumMateEnt)

         For i = 0 To nNumMateEnt - 1

             swMateEnt(i) = swMate.MateEntity(i)
             swComp = swMateEnt(i).ReferenceComponent

             vMateEntPar = swMateEnt(i).EntityParams

             Debug.Print("      RefType(" & i & ")   = " & swMateEnt(i).ReferenceType)
             Debug.Print("        Component          = " & swComp.Name2   " (" & swComp.ReferencedConfiguration & ") --> " & swComp.GetPathName)
             Debug.Print("        Point              = (" & vMateEntPar(0) * 1000.0#   ", " & vMateEntPar(1) * 1000.0# & ", " & vMateEntPar(2) * 1000.0# & ") mm")
             Debug.Print("        Vector             = (" & vMateEntPar(3)   ", " & vMateEntPar(4) & ", " & vMateEntPar(5) & ")")
             Debug.Print("        Radius 1           = " & vMateEntPar(6) * 1000.0# & " mm")
             Debug.Print("        Radius 2           = " & vMateEntPar(7) * 1000.0# & " mm")

         Next i

         Select Case swMate.Type

             Case swMateType_e.swMateGEAR
                 ' Cannot change alignment on these mate types
                 Exit Sub

         End Select

         If swMateAlign_e.swMateAlignALIGNED = swMate.Alignment  Then
             nNewMateAlign = swMateAlign_e.swMateAlignANTI_ALIGNED
         Else

             If swMateAlign_e.swMateAlignANTI_ALIGNED = swMate.Alignment  Then
                 nNewMateAlign = swMateAlign_e.swMateAlignALIGNED

             Else

                 Exit Sub

             End If

         End If

         swModel.ClearSelection2(True)

         For i = 0 To nNumMateEnt - 1

             '   IAssemblyDoc::EditMate3 requires that mate entities
             '   be selected with mark of 1 except for:
             '       swMateCAMFOLLOWER
             '           cam face              --> 1
             '           cam follower face     --> 8
             '       swMateSYMMETRIC
             '           symmetry faces        --> 1
             '           symmetry plane        --> 4

             bRet = SelectMateEntity(swApp, swModel, swMateEnt(i), 1)

         Next i

         ' IAssemblyDoc::EditMate3 requires mate feature to be selected last
         ' Mark is ignored
         bRet = swFeat.Select2(True, 0)

         swAssy.EditMate3( _
             swMate.Type, _
             nNewMateAlign, _
             True, _
             nMateDist, _
             swMate.MaximumVariation, _
             swMate.MinimumVariation, _
             0.0#, _
             0.0#, _
             nMateDist, _
             swMate.MaximumVariation, _
             swMate.MinimumVariation, _
             False, _
             True, _
             0, _
             nRetVal)

         bRet = swModel.EditRebuild3

     End Sub

     Public swApp As SldWorks

 End  Class
```
