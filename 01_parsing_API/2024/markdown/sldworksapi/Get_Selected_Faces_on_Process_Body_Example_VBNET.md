---
title: "Get Selected Faces on Processed Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selected_Faces_on_Process_Body_Example_VBNET.htm"
---

# Get Selected Faces on Processed Body Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
        Const RadPerDeg As Double = 1.0# / 57.3
        Const MaxUAngle As Double = 1.0# * RadPerDeg
        Const MaxVAngle As Double = 1.0# * RadPerDeg

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swBody As Body2
        Dim swProcBody As Body2
        Dim swPart As PartDoc
        Dim swNewPart As PartDoc
        Dim swFeat As Feature
        Dim vBodies(0) As Object
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim status As Boolean
        Dim swBodyVar(0) As Object
        Dim swSelFaceVar(3) As Object
        Dim swSelFaceCount As Integer

        'Open part
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swPart = swModel

        'Get and process body in part
        vBodies = swPart.GetBodies2(swBodyType_e.swSolidBody, False)
        swBody = vBodies(0)
        swProcBody = swBody.GetProcessedBody2(MaxUAngle, MaxVAngle)

        'Create new part containing processed body
        swNewPart = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\part.prtdot", 0, 0, 0)
        swFeat = swNewPart.CreateFeatureFromBody3(swProcBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)
        Debug.Print("Original part: " & swModel.GetPathName)
        Debug.Print("  Title: " & swModel.GetTitle)
        Debug.Print("    Body faces: " & swBody.GetFaceCount)
        Debug.Print("    Processed body faces: " & swProcBody.GetFaceCount)

        'Select multiple faces in new part
        swModel = swNewPart
        Debug.Print("New part title: " & swModel.GetTitle)
        Debug.Print("    Body faces: " & swBody.GetFaceCount)
        Debug.Print("    Processed body faces: " & swProcBody.GetFaceCount)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", -0.0258707587273648, -0.00453920675113295, -0.00750000000022055, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.016247803762667, 0, -0.0112417538793466, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0149546544521968, -0.026689891165347, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0208314165242882, -0.0200000000001523, -0.00322480979224338, True, 0, Nothing, 0)

        'Get selected faces in body
        swBodyVar = swNewPart.GetBodies2(swBodyType_e.swAllBodies, True)
        If IsNothing(swBodyVar) Then
            Debug.Print("    Did not get any bodies.")
        Else
            swBody = swBodyVar(0)
            Debug.Print("    Name of processed body: " & swBody.Name)
        End If
        swProcBody = swBody.GetProcessedBodyWithSelFace
        swSelFaceVar = swProcBody.GetSelectedFaces
        If Not IsNothing(swSelFaceVar) Then
            swSelFaceCount = swProcBody.GetSelectedFaceCount
            Debug.Print("      Number of faces selected in processed body: " & swSelFaceCount)
        Else
            Debug.Print("      No faces selected in processed body.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
