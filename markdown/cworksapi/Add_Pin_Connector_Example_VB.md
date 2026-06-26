---
title: "Add Pin Connector Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Pin_Connector_Example_VB.htm"
---

# Add Pin Connector Example (VBA)

This example shows how to add a pin connector to a static study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation  version type library).
 ' 3. Ensure that the specified material library exists.
 ' 4. Open public_documents\samples\Simulation Examples\pliers.sldasm.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the model.
 ' 2. Activates the Ready study.
 ' 3. Deletes the pin between branches connector.
 ' 4. Adds Pin Connector-3 to the Connectors folder in the Simulation study
 '    tree.
 ' 5. Prints the properties of Pin Connector-3 to the Immediate window.
 ' 6. Meshes the model.
 ' 7. Analyzes Ready.
 ' 8. Inspect the Immediate window, the Simulation Study tree, and the
 '    graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Dim SwApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
 Dim COSMOSObject As CosmosWorksLib.CwAddincallback
 Dim ActDoc As CosmosWorksLib.CWModelDoc
 Dim StudyMngr As CosmosWorksLib.CWStudyManager
 Dim Study As CosmosWorksLib.CWStudy
 Dim lrMngr As CosmosWorksLib.CWLoadsAndRestraintsManager
 Dim pinConnector As CosmosWorksLib.CWPinConnector
 Dim CwMesh As CosmosWorksLib.CwMesh
 Dim str3 As String, str4 As String
 Dim varArray1 As Variant, varArray2 As Variant
 Dim pDisp3 As Object, pDisp4 As Object
 Dim var20 As Variant, var21 As Variant
 Dim errCode As Long
 Dim el As Double, tl As Double
 Dim longstatus As Long
Option Explicit

Sub main()
    Set SwApp = Application.SldWorks
     Set Part = SwApp.ActiveDoc
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "Failed to get Simulation add-in"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "Failed to get COSMOSWORKS"
    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get active document"
    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get study manager"
    Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to get frequency study"

    StudyMngr.ActiveStudy = 0

    str3 = "64,31,0,0,3,0,0,0,255,254,255,22,115,0,101,0,99,0,111,0,110,0,100,0,32,0,98,0,114,0,97,0,110,0,99,0,104,0,45,0,49,0,64,0,112,0,108,0,105,0,101,0,114,0,115,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,12,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,84,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,10"
     str3 = str3 & "1,0,115,0,92,0,115,0,101,0,99,0,111,0,110,0,100,0,32,0,98,0,114,0,97,0,110,0,99,0,104,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,13,115,0,101,0,99,0,111,0,110,0,100,0,32,0,98,0,114,0,97,0,110,0,99,0,104,0,2,0,0,164,247,240,62,0,33,23,28,65,1,0,0,0,0,0,0,0,4,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,33,23,28,65,29,0,0,0,70,252,240,62,34,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,29,0,0,0,70,252,240,62,0,0,0,0,1,0,0,0,0,0,255,255,1,0,24,0,109,111,69,110,100,70,97,99,101,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,39,0,0,0,85,255,240,62,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     str3 = str3 & ",Type=1"
    str4 = "64,31,0,0,3,0,0,0,255,254,255,21,102,0,105,0,114,0,115,0,116,0,32,0,98,0,114,0,97,0,110,0,99,0,104,0,45,0,49,0,64,0,112,0,108,0,105,0,101,0,114,0,115,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,83,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0"
     str4 = str4 & ",115,0,92,0,102,0,105,0,114,0,115,0,116,0,32,0,98,0,114,0,97,0,110,0,99,0,104,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,12,102,0,105,0,114,0,115,0,116,0,32,0,98,0,114,0,97,0,110,0,99,0,104,0,2,0,0,164,247,240,62,0,1,22,28,65,1,0,0,0,0,0,0,0,6,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,1,22,28,65,29,0,0,0,70,252,240,62,34,0,0,0,255,255,1,0,24,0,109,111,69,110,100,70,97,99,101,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,38,0,0,0,165,255,240,62,1,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,29,0,0,0,70,252,240,62,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0"
     str4 = str4 & ",Type=1"

     StringtoArray str3, var20
     Set pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), longstatus)
    StringtoArray str4, var21
     Set pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), longstatus)
    varArray1 = Array(pDisp3)
     varArray2 = Array(pDisp4)
    Set lrMngr = Study.LoadsAndRestraintsManager
     lrMngr.DeleteLoadsAndRestraints "pin between branches"

    ' Add pin connector
     Set pinConnector = lrMngr.AddPinConnector((varArray1), (varArray2), errCode)

     pinConnector.PinConnectorBeginEdit

    pinConnector.IncludeStrengthData = True
     pinConnector.MaterialType = 1
     pinConnector.SetLibraryMaterial "c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Alloy Steel"
     pinConnector.TensileStressAreaValue = 1
     pinConnector.PinStrengthValue = 620422000

    Debug.Print "Number of entities in Pin Connector-3"
     Debug.Print "   At first location: " & pinConnector.GetFirstLocationEntityCount
     Debug.Print "   At second location: " & pinConnector.GetSecondLocationEntityCount

    errCode = pinConnector.PinConnectorEndEdit

    Debug.Print "Units of axial and rotational stiffness as defined in swsUnitSystem_e: " & pinConnector.Unit

    Debug.Print "Prevent relative rotation between cylindrical faces? " & pinConnector.IncludeTypeWithKey
     If pinConnector.IncludeTypeWithKey Then
         Debug.Print "   Axial stiffness: " & pinConnector.AxialStiffnessValue
     End If

    Debug.Print "Prevent relative axial translation between cylindrical faces? " & pinConnector.IncludeTypeWithRetainerRing
     If pinConnector.IncludeTypeWithRetainerRing Then
         Debug.Print "   Rotational stiffness: " & pinConnector.RotationalStiffnessValue
     End If

    Debug.Print "Include mass in the analysis? " & pinConnector.IncludeMass
     If pinConnector.IncludeMass Then
         Debug.Print "  Mass: " & pinConnector.MassValue
     End If
     Debug.Print "Include strength data in the analysis? " & pinConnector.IncludeStrengthData

    If pinConnector.IncludeStrengthData Then
         Debug.Print "Material data:"
         Dim libName As String, materialName As String
         pinConnector.PinConnectorBeginEdit
         pinConnector.GetLibraryMaterial libName, materialName
         pinConnector.PinConnectorEndEdit
         Debug.Print "   Source (1=library, 0=user-defined): " & pinConnector.MaterialType
         Debug.Print "   Library: " & libName
         Debug.Print "   Name: " & materialName
         Debug.Print "   Units as defined in swsUnitSystem_e: " & pinConnector.MaterialUnit
         Debug.Print "   Poisson's Ratio: " & pinConnector.PoissonsRatio
         Debug.Print "   Young's Modulus: " & pinConnector.YoungModulus
         Debug.Print "   Coefficient of thermal expansion: " & pinConnector.ThermalCoefficient
         Debug.Print "   Mass: " & pinConnector.MassValue
     End If

        Debug.Print "Strength data:"
         Debug.Print "   Tensile stress area: " & pinConnector.TensileStressAreaValue
         Debug.Print "      Units as defined in swsTensileStressAreaUnit_e: " & pinConnector.TensileStressAreaUnit
         Debug.Print "   Pin strength: " & pinConnector.PinStrengthValue
         Debug.Print "      Units as defined in swsStrengthUnit_e: " & pinConnector.PinStrengthUnit
         Debug.Print "   Safety factor: " & pinConnector.SafetyFactor

    ' Mesh model
     Set CwMesh = Study.Mesh
     If CwMesh Is Nothing Then ErrorMsg SwApp, "Failed to get mesh object"
    CwMesh.Quality = 1
     Call CwMesh.GetDefaultElementSizeAndTolerance(swsLinearUnitMillimeters, el, tl)
    errCode = Study.CreateMesh(swsLinearUnitMillimeters, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create mesh"

    ' Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed"

 End Sub
Sub StringtoArray(inputSTR As String, varEntity As Variant)
   Dim PID() As Byte
    Dim i As Integer
   varEntity = Split(inputSTR, ",")
    ReDim PID(UBound(varEntity))
   For i = 0 To (UBound(varEntity) - 1)
       PID(i) = varEntity(i)
    Next i
   varEntity = PID
End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
   SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""

End Sub
```
