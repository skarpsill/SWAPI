---
title: "Get Mate Definition Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mate_Definition_Example_VB.htm"
---

# Get Mate Definition Example (VBA)

This example shows how to retrieve the mate definition.

```
'-----------------------------------------------
' Preconditions:
' 1. Open an assembly document containing mates.
' 2. Select a mate.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the mate definition.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub ProcessDisplayDimension(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swDispDim As SldWorks.DisplayDimension, nVarFactor As Double, sVarType As String)
    Dim swDim As SldWorks.Dimension
    Dim vDimValueArr As Variant
```

```
    If Nothing Is swDispDim Then
        Debug.Print "     No display dimension"
        Debug.Print " "
        Exit Sub
    End If
```

```
    Set swDim = swDispDim.GetDimension
```

```
    vDimValueArr = swDim.GetSystemValue3(swThisConfiguration, Empty)
    Debug.Assert Not IsEmpty(vDimValueArr)
    Debug.Assert 0 = UBound(vDimValueArr)
```

```
    ' Show name and value of dimension
    Debug.Print "      Dim Name      = " & swDim.FullName
    Debug.Print "      Dim Value     = " & vDimValueArr(0) * nVarFactor & sVarType
    Debug.Print " "
```

```
End Sub
```

```
Sub ProcessMateEntity(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swMateEnt As SldWorks.MateEntity2)
    Dim swComp As SldWorks.Component2
    Dim vEntParam As Variant
```

```
    If Nothing Is swMateEnt Then
        Debug.Print "      No mate entity"
        Debug.Print " "
        Exit Sub
    End If
```

```
    Set swComp = swMateEnt.ReferenceComponent
```

```
    vEntParam = swMateEnt.EntityParams
    Debug.Assert Not IsEmpty(vEntParam)
    Debug.Assert 7 = UBound(vEntParam)
```

```
    ' Show name of mate component entity and its parameters
    Debug.Print "      Ref Comp  = " & swComp.Name2
    Debug.Print "      Location  = (" & vEntParam(0) * 1000# & ", " & vEntParam(1) * 1000# & ", " & vEntParam(2) * 1000# & ") mm"
    Debug.Print "      (i, j, k) = (" & vEntParam(3) & ", " & vEntParam(4) & ", " & vEntParam(5) & ")"
    Debug.Print "      Radius 1  = " & vEntParam(6) * 1000# & " mm"
    Debug.Print "      Radius 2  = " & vEntParam(7) * 1000# & " mm"
    Debug.Print " "
```

```
End Sub
```

```
Sub ProcessMate(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swMate As SldWorks.Mate2)
    Dim sVarType As String
    Dim nVarFactor As Double
    Dim nNumMateEnt As Long
    Dim i As Long
```

```
    ' Get the number of entities for the selected mate
    nNumMateEnt = swMate.GetMateEntityCount
```

```
    ' If mate type is Angle or Distance, then set conversion values
    Select Case swMate.Type
        Case swMateANGLE
            ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
            sVarType = " deg"
            nVarFactor = 57.3
        Case swMateDISTANCE
            sVarType = " mm"
            nVarFactor = 1000#
    End Select
```

```
    ' Show if mate is aligned and can be flpped
    Debug.Print "    Alignment          = " & swMate.Alignment
    Debug.Print "    CanBeFlipped       = " & swMate.CanBeFlipped
```

```
    ' If mate is Angle or Distance, show variances
    If swMateANGLE = swMate.Type Or swMateDISTANCE = swMate.Type Then
        Debug.Print "    MaximumVariation   = " & swMate.MaximumVariation * nVarFactor & sVarType
        Debug.Print "    MinimumVariation   = " & swMate.MinimumVariation * nVarFactor & sVarType
    End If
```

```
    ' Show type of mate
    Debug.Print "    Type               = " & swMate.Type
```

```
    ProcessDisplayDimension swApp, swModel, swMate.DisplayDimension, nVarFactor, sVarType
```

```
    For i = 0 To nNumMateEnt - 1
        ProcessMateEntity swApp, swModel, swMate.MateEntity(i)
    Next i
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swMate As SldWorks.Mate2
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swMate = swFeat.GetSpecificFeature2
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' Show name of selected feature (in this case, a mate) and name of feature
    Debug.Print "  " & swFeat.Name & " [" & swFeat.GetTypeName & "]"
```

```
    ProcessMate swApp, swModel, swMate
```

```
End Sub
```
