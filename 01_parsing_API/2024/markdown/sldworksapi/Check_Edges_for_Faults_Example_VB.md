---
title: "Check Edges for Faults Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Edges_for_Faults_Example_VB.htm"
---

# Check Edges for Faults Example (VBA)

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
'----------------------------------------------------------------------------
Option Explicit
```

```
Function GetStringFromID(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vPIDarr As Variant) As String
    Dim vPID As Variant
```

```
    For Each vPID In vPIDarr
        GetStringFromID = GetStringFromID & Format(vPID, "###000")
    Next vPID
End Function
```

```
Sub ProcessFaultEntity(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swEdge As SldWorks.Edge, swFaultEnt As SldWorks.FaultEntity)
    Dim swModExt As SldWorks.ModelDocExtension
    Dim vPIDarr As Variant
    Dim nCount As Long
    Dim swEnt As SldWorks.Entity
    Dim bRet As Boolean
    Dim i As Long
```

```
    nCount = swFaultEnt.Count
    ' For each edge, print:
    ' * no fault found, if not fault found
    ' * edge ID and error code, if fault found
    If 0 = nCount Then
        Debug.Print "      No fault found."
        Exit Sub
    End If
    Set swModExt = swModel.Extension
    vPIDarr = swModExt.GetPersistReference3(swEdge): Debug.Assert Not IsEmpty(vPIDarr)
    Debug.Print "    Edge ID = " & GetStringFromID(swApp, swModel, vPIDarr)
```

```
    For i = 0 To nCount - 1
        Set swEnt = swFaultEnt.Entity(i)
        If Not swEnt Is Nothing Then
            bRet = swEnt.Select4(True, Nothing): Debug.Assert bRet
        End If
        Debug.Print "      Fault[" & i & "]                         = " & swFaultEnt.ErrorCode(i)
    Next i
```

```
End Sub
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim vBodyArr As Variant
    Dim vBody As Variant
    Dim swBody As SldWorks.Body2
    Dim nRetval1 As Long
    Dim nRetval2 As Long
    Dim vEdgeArr As Variant
    Dim vEdge  As Variant
    Dim swEdge As SldWorks.Edge
    Dim swFaultEnt As SldWorks.FaultEntity
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    vBodyArr = swPart.GetBodies2(swAllBodies, True): Debug.Assert Not IsEmpty(vBodyArr)
    For Each vBody In vBodyArr
        Set swBody = vBody
        Debug.Print "  Body[" & swBody.GetType & "] --> " & swBody.GetSelectionId
        nRetval1 = swBody.Check ' Obsolete method
        nRetval2 = swBody.Check2 ' Obsolete method
        Debug.Print "    IBody2::Check (1 if valid; 0 if not) = " & nRetval1
        Debug.Print "    IBody2::Check2(Number of faults) = " & nRetval2
```

```
        vEdgeArr = swBody.GetEdges
        If Not IsEmpty(vEdgeArr) Then
                For Each vEdge In vEdgeArr
                    Set swEdge = vEdge
                    Set swFaultEnt = swEdge.Check
                    ProcessFaultEntity swApp, swModel, swEdge, swFaultEnt
                Next vEdge
        Else
            Debug.Print "      No edges in part."
        End If
    Next vBody
```

```
End Sub
```
