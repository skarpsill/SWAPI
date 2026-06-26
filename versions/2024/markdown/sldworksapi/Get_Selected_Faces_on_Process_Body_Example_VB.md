---
title: "Get Selected Faces on Processed Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selected_Faces_on_Process_Body_Example_VB.htm"
---

# Get Selected Faces on Processed Body Example (VBA)

This example shows how to get the selected faces on a processed body.

```
'------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template
'    and part exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Creates a new part with an imported body
'    from the processed body of the original part.
' 3. Gets the body in the new part and selects
'    multiple faces on that body.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'--------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
    Const RadPerDeg As Double = 1# / 57.3
    Const MaxUAngle As Double = 1# * RadPerDeg
    Const MaxVAngle As Double = 1# * RadPerDeg
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swBody As SldWorks.Body2
    Dim swProcBody As SldWorks.Body2
    Dim swPart As SldWorks.PartDoc
    Dim swNewPart As SldWorks.PartDoc
    Dim swFeat As SldWorks.Feature
    Dim vBodies As Variant
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
    Dim status As Boolean
    Dim swBodyVar As Variant
    Dim swSelFaceVar As Variant
    Dim swSelFaceCount As Long
```

```
    Set swApp = Application.SldWorks
```

```
    'Open part
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swPart = swModel
```

```
    'Get and process body in part
    vBodies = swPart.GetBodies2(swSolidBody, False)
    Set swBody = vBodies(0)
    Set swProcBody = swBody.GetProcessedBody2(MaxUAngle, MaxVAngle)
```

```
    'Create new part containing processed body
    Set swNewPart = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\part.prtdot", 0, 0, 0)
    Set swFeat = swNewPart.CreateFeatureFromBody3(swProcBody, False, swCreateFeatureBodyCheck)
    Debug.Print "Original part: " & swModel.GetPathName
    Debug.Print "  Title: " & swModel.GetTitle
    Debug.Print "    Body faces: " & swBody.GetFaceCount
    Debug.Print "    Processed body faces: " & swProcBody.GetFaceCount
```

```
    'Select multiple faces in new part
    Set swModel = swNewPart
    Debug.Print "New part title: " & swModel.GetTitle
    Debug.Print "    Body faces: " & swBody.GetFaceCount
    Debug.Print "    Processed body faces: " & swProcBody.GetFaceCount
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", -2.58707587273648E-02, -4.53920675113295E-03, -7.50000000022055E-03, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -0.016247803762667, 0, -1.12417538793466E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -1.49546544521968E-02, -0.026689891165347, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -2.08314165242882E-02, -2.00000000001523E-02, -3.22480979224338E-03, True, 0, Nothing, 0)
```

```
    'Get selected faces in processed body
    swBodyVar = swNewPart.GetBodies2(swAllBodies, True)
    If IsEmpty(swBodyVar) Then
        Debug.Print "    Did not get any bodies."
    Else
        Set swBody = swBodyVar(0)
        Debug.Print "    Name of processed body: " & swBody.Name
    End If
    Set swProcBody = swBody.GetProcessedBodyWithSelFace
    swSelFaceVar = swProcBody.GetSelectedFaces
    If Not IsEmpty(swSelFaceVar) Then
        swSelFaceCount = swProcBody.GetSelectedFaceCount
        Debug.Print "      Number of faces selected in processed body: " & swSelFaceCount
    Else
        Debug.Print "      No faces selected in processed body."
    End If
```

```
End Sub
```
