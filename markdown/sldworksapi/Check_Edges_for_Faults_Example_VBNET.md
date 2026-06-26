---
title: "Check Edges for Faults Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Edges_for_Faults_Example_VBNET.htm"
---

# Check Edges for Faults Example (VB.NET)

This example shows how to check the edges in a part for faults.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Checks the bodies and edges in the part.
' 2. Examine the Immediate window.
'-----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim vBodyArr As Object
        Dim vBody As Object
        Dim swBody As Body2
        Dim nRetval1 As Integer
        Dim nRetval2 As Integer
        Dim vEdgeArr As Object
        Dim vEdge As Object
        Dim swEdge As Edge
        Dim swFaultEnt As FaultEntity

        swModel = swApp.ActiveDoc
        swPart = swModel
        Debug.Print("File = " & swModel.GetPathName)
        vBodyArr = swPart.GetBodies2(swBodyType_e.swAllBodies, True) : Debug.Assert(Not IsNothing(vBodyArr))
        For Each vBody In vBodyArr
            swBody = vBody
            Debug.Print("  Body[" & swBody.GetType & "] --> " & swBody.GetSelectionId)
            nRetval1 = swBody.Check ' Obsolete method
            nRetval2 = swBody.Check2 ' Obsolete method
            Debug.Print("    IBody2::Check (1 if valid; 0 if not) = " & nRetval1)
            Debug.Print("    IBody2::Check2(Number of faults) = " & nRetval2)
            vEdgeArr = swBody.GetEdges
            If Not IsNothing(vEdgeArr) Then
                For Each vEdge In vEdgeArr
                    swEdge = vEdge
                    swFaultEnt = swEdge.Check
                    ProcessFaultEntity(swApp, swModel, swEdge, swFaultEnt)
                Next vEdge
            Else
                Debug.Print("      No edges in part.")
            End If
        Next vBody

    End Sub

    Function GetStringFromID(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal vPIDarr As Object) As String
        Dim vPID As Object
        GetStringFromID = ""
        For Each vPID In vPIDarr
            GetStringFromID = GetStringFromID & Format(vPID, "###000")
        Next vPID
    End Function

    Sub ProcessFaultEntity(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swEdge As Edge, ByVal swFaultEnt As FaultEntity)
        Dim swModExt As ModelDocExtension
        Dim vPIDarr As Object
        Dim nCount As Integer
        Dim swEnt As Entity
        Dim bRet As Boolean
        Dim i As Integer

        nCount = swFaultEnt.Count
        ' For each edge, print:
        ' * no fault found, if no fault found
        ' * edge ID and error code, if fault found
        If 0 = nCount Then
            Debug.Print("      No fault in edge.")
            Exit Sub
        End If

        swModExt = swModel.Extension
        vPIDarr = swModExt.GetPersistReference3(swEdge) : Debug.Assert(Not IsNothing(vPIDarr))
        Debug.Print("    Edge ID = " & GetStringFromID(swApp, swModel, vPIDarr))
        For i = 0 To nCount - 1
            swEnt = swFaultEnt.Entity(i)
            If Not swEnt Is Nothing Then
                bRet = swEnt.Select4(True, Nothing) : Debug.Assert(bRet)
            End If
            Debug.Print("      Fault[" & i & "]                         = " & swFaultEnt.ErrorCode(i))
        Next i
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
