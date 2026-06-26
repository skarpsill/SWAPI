---
title: "Check Bodies for Faults Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Bodies_for_Faults_Example_VB.htm"
---

# Check Bodies for Faults Example (VBA)

This example shows how to check the solid and sheet bodies in a part for faults.

```
'--------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Checks the bodies in the part document.
' 2. Examine the Immediate window.
'--------------------------------------------------
Option Explicit
```

```
Sub ProcessFaultEntity(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swFaultEnt As SldWorks.FaultEntity)
    Dim nCount As Long
    Dim swEnt As SldWorks.Entity
    Dim bRet As Boolean
    Dim i  As Long
```

```
    nCount = swFaultEnt.Count: If 0 = nCount Then Exit Sub 'Else print the error code for each fault
    For i = 0 To nCount - 1
        Set swEnt = swFaultEnt.Entity(i)
        If Not swEnt Is Nothing Then
            bRet = swEnt.Select4(True, Nothing): Debug.Assert bRet
        End If
        Debug.Print "    Fault[" & i & "] = " & swFaultEnt.ErrorCode(i)
    Next i
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
    Dim swFaultEnt  As SldWorks.FaultEntity
    Dim i As Long
    Dim bRet As Boolean
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
        Set swFaultEnt = swBody.Check3
        Debug.Print "  Body[" & swBody.GetType & "] --> " & swBody.GetSelectionId
        nRetval1 = swBody.Check 'Obsolete method
        nRetval2 = swBody.Check2 'Obsolete method
        Debug.Print "    IBody2::Check (1 if valid; 0 if not) = " & nRetval1
        Debug.Print "    IBody2::Check2(Number of faults) = " & nRetval2
        ProcessFaultEntity swApp, swModel, swFaultEnt
    Next vBody
```

```
End Sub
```
