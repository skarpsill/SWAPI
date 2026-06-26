---
title: "Add Bearing Connector Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Bearing_Connector_Example_VBNET.htm"
---

# Add Bearing Connector Example (VB.NET)

This example shows how to add a bearing connector for a shaft and its
housing.

NOTE:To get persistent reference
identifiers (PIDs) for model selections, you can use[pidcollector.exe](GettingStarted-swsimulationapi.html)or IModelDocExtension::GetPersistReference3.

'====================================================

'Preconditions:

'1. Contact SOLIDWORKS
API Support to obtain the assembly and components that work
with this macro.

'2. Open QAA_01_Cylindrical Bearing.sldasm in SOLIDWORKS.

'3. Load the Simulation
add-in in SOLIDWORKS.

'4. Add the SOLIDWORKS
Simulation interop assembly as a reference to the .NET macro.

'5 (Optional) Uncomment
code to get connector forces.

'6. Open an Immediate
window.

'

'Postconditions:

'1. Activates and gets
the Static 5_Rigid study.

'2. Creates Bearing Connector-2 and modifies its properties.

'3. Meshes the model.

'4. Analyzes the study.

'5. Inspect the
Immediate window and the Simulation study tree.

'======================================================

ImportsSolidWorks.Interop.sldworks

ImportsSolidWorks.Interop.cosworks

ImportsSolidWorks.Interop.swconst

ImportsSystem.Runtime.InteropServices

ImportsSystem

PartialClassSolidWorksMacro

DimPartAsModelDoc2

DimswAssemblyAsAssemblyDoc

DimmyModelViewAsModelView

DimboolstatusAsBoolean

DimlongstatusAsInteger,
longwarningsAsInteger

PublicSubmain()

DimCOSMOSWORKSObjAsCosmosWorks

DimCWAddinCallBackObjAsCwAddincallback

DimActiveDocObjAsCWModelDoc

DimStudyManagerObjAsCWStudyManager

DimCWMeshAsCWMesh

DimCWResultAsCWResults

DimLoadsAndRestraintsManagerObjAsCWLoadsAndRestraintsManager

DimerrCodeAsInteger

DimelAsDouble, tlAsDouble, Tol1AsDouble,
Connector_ForceAsDouble

'Set Part =
SwApp.OpenDoc6("QAA_01_Cylindrical Bearing.SLDASM", swDocASSEMBLY, 192, "",
longstatus, longwarnings)

'If Part Is Nothing Then
ErrorMsg2( SwApp, "Failed to open:QAA_01_Cylindrical Bearing.SLDASM", True)

'Set swAssembly = Part

'SwApp.ActivateDoc2
("QAA_01_Cylindrical Bearing.SLDASM", False, longstatus)

Part = swApp.ActiveDoc

CWAddinCallBackObj = swApp.GetAddInObject("CosmosWorks.CosmosWorks")

IfCWAddinCallBackObjIsNothingThenErrorMsg2(swApp,"CWAddinCallBackObj object not found",True)

COSMOSWORKSObj = CWAddinCallBackObj.CosmosWorks

IfCOSMOSWORKSObjIsNothingThenErrorMsg2(swApp,"COSMOSWORKSObj object not found",True)

myModelView = Part.ActiveView

myModelView.FrameLeft = 0

myModelView.FrameTop = 0

myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

ActiveDocObj = COSMOSWORKSObj.ActiveDoc()

IfActiveDocObjIsNothingThenErrorMsg2(swApp,"No Active Document",True)

StudyManagerObj = ActiveDocObj.StudyManager()

IfStudyManagerObjIsNothingThenErrorMsg2(swApp,"StudyManagerObj object not there",True)

StudyManagerObj.ActiveStudy = 1

DimStudyObjAsObject

StudyObj = StudyManagerObj.GetStudy(1)

IfStudyObjIsNothingThenErrorMsg2(swApp,"Study not created",True)

Part.GraphicsRedraw2

Part.ViewZoomTo2(0.0539264773386334, 0.0194101535368661, 0.159999999986677,
0.0933821942296391, -0.0238032506770925, 0.159999999986677)

Part.GraphicsRedraw2

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(-0.0430154869025614,
-0.0023147631828806, 0.00869723354912821, -0.851450358677067,
-0.352944394561843, -0.387895012930133, 0.000163979435633325, 2,True, 0, 0)

Part.GraphicsRedraw2

Part.GraphicsRedraw2()

Part.GraphicsRedraw2

Part.GraphicsRedraw2

boolstatus = Part.Extension.SelectByRay(-0.0445748406675648,
-0.00987194045754336, 0.00485229755915384, -0.851450358677067,
-0.352944394561843, -0.387895012930133, 0.000163979435633325, 2,True, 0, 0)

Part.GraphicsRedraw2

Part.GraphicsRedraw2

LoadsAndRestraintsManagerObj = StudyObj.LoadsAndRestraintsManager()

DimDispatchShaftObjAsObject

DispatchShaftObj = Part.SelectionManager.GetSelectedObject6(1, -1)

DimDispatchHousingObjAsObject

DispatchHousingObj =
Part.SelectionManager.GetSelectedObject6(2, -1)

DimCWBearingConnectorAsICWBearingConnector

CWBearingConnector = LoadsAndRestraintsManagerObj. AddBearingConnector (DispatchShaftObj,
DispatchHousingObj, errCode)

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector creation failed",True)

IfCWBearingConnectorIsNothingThenErrorMsg2(swApp,"Bearing connector creation failed",True)

errCode = CWBearingConnector. PerformAdvanceValidations

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector PerformAdvanceValidations failed",True)

CWBearingConnector = LoadsAndRestraintsManagerObj. GetBearingConnector ("Bearing Connector-2",
errCode)

IfCWBearingConnectorIsNothingThenErrorMsg2(swApp,"GetBearingConnector failed",True)

CWBearingConnector. BeginEdit ()

CWBearingConnector. ConnectionType =
swsBearingConnectionType_e.swsSpringConnType

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector ConnectionType failed",True)

CWBearingConnector. UnitType = swsUnit_e.swsUnitSI

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector UnitType failed",True)

CWBearingConnector. StiffnessType =
swsBearingStiffnessType_e.swsBearingStiffnessRigid

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector StiffnessType failed",True)

CWBearingConnector. AxialStiffnessValue = 0

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector AxialStiffnessValue failed",True)

CWBearingConnector. LateralStiffnessValue = 0

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector LateralStiffnessValue failed",True)

CWBearingConnector. TiltStiffnessValue = 0

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector TiltStiffnessValue failed",True)

CWBearingConnector. StabilizeShaftRotation =False

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector StabilizeShaftRotation failed",True)

errCode = CWBearingConnector. EndEdit ()

IferrCode <> 0ThenErrorMsg2(swApp,"Bearing connector EndEdit failed",True)

Part.ClearSelection2(True)

CWMesh = StudyObj.Mesh

IfCWMeshIsNothingThenErrorMsg2(swApp,"No Mesh Object",False)

CWMesh.Quality = 1

CWMesh.MesherType = 0

CallCWMesh.GetDefaultElementSizeAndTolerance(0, el, tl)

errCode = StudyObj.CreateMesh(0, el, tl)

IferrCode <> 0ThenErrorMsg2(swApp,"Mesh failed",True)

errCode = StudyObj.RunAnalysis

IferrCode <> 0ThenErrorMsg2(swApp,"Analysis failed",True)

Part.GraphicsRedraw2

CWResult = StudyObj.Results

IfCWResultIsNothingThenErrorMsg2(swApp,"No Result Object",False)

'Get Connector results

'Dim Forc As Variant

'Forc =
CWResult.GetConnectorForces2(1, "Bearing connector-2", 0, errCode)

'Connector_Force = -528.28 'Expected axial force (comp = 7)

'Tol1 = 0.1

'Dim i As Integer

'For i = 0 To 10

' Debug.Print i & " : " & Forc(i)

' SwApp.RecordLine( "'******** Bearing connector Force " & i & " : " &
Forc(i) & " ********")

'Next i

'If errCode <> 0 Then
ErrorMsg2( SwApp, "No connector force", True)

'Connector force comparision.

'If ((Forc(7)) = nan) Then

' ErrorMsg2( SwApp,
"Forc(7) is not calculated ", False)

'End If

'If ((Forc(7)) < 0.95 *
Connector_Force) Or ((Forc(7)) > 1.05 * Connector_Force) Then

' ErrorMsg2( SwApp,
"O/p Force % error = " & (((Forc(7) - Connector_Force) / Connector_Force) *
100), False)

'End If

EndSub

SubErrorMsg2(SwAppAsObject,
MessageAsString,
EndTestAsBoolean)

SwApp.SendMsgToUser2(Message, 0, 0)

SwApp.RecordLine("'***
WARNING - General")

SwApp.RecordLine("'***
"& Message)

SwApp.RecordLine("")

'If EndTest Then

'SwApp.ExitApp

'End

'End If

EndSub

'''<summary>

'''The SldWorks swApp variable is
pre-assigned for you.

'''</summary>

PublicswAppAsSldWorks

EndClass
