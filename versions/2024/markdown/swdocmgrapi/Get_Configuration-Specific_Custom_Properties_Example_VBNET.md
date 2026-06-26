---
title: "Get Configuration-Specific Custom Properties for Components (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Configuration-Specific_Custom_Properties_Example_VBNET.htm"
---

# Get Configuration-Specific Custom Properties for Components (VB.NET)

This example shows how to get custom properties for
assembly components.

'---------------------------------------------------------------------------

' Preconditions:

' 1. Read the SOLIDWORKS
Document Manager API Getting Started

' topic and ensure that the required DLLs are registered.

' 2. Copy and paste this
code into a VB.NET console application

' in Microsoft Visual Studio.

' 3. Ensure the Solution
Platform is of type x64.

' 4. Add the SolidWorks.Interop.swdocumentmgr.dll reference to the project:

' a. Right-click the solution in Solution Explorer.

' b. Click Add Reference .

' c. Click Browse .

' d. Click:

' install_dir \api\redist\SolidWorks.Interop.swdocumentmgr.dll

' e. Click Add .

' f. Click Close .

' 5. Add the Microsoft Scripting Runtime reference to the project.

' 6. Ensure that the
model(s) to open exists and is(are) not readonly.

' 7. Substitute your_license_key with your SOLIDWORKS Document

' Manager license key.

' 8. Open the Immediate
window.

'

' Postconditions:

' 1. Gets document-level,
component-level, and configuration-level custom properties for all assembly
components.

' 2. Inspect the
Immediate window.

'

'--------------------------------------------------------------------------

ImportsSystem.Diagnostics

ImportsSolidWorks.Interop.swdocumentmgr

ModuleModule1

SubMain()

DimswDocMgrAsSwDMApplication

DimswCfAsSwDMClassFactory

swCf = CreateObject("SwDocumentMgr.SwDMClassFactory")

DimsKeyAsString

sKey =" your_license_key"

swDocMgr = swCf.GetApplication(sKey)

DimswDmSearchOptAsSwDMSearchOption

swDmSearchOpt = swDocMgr.GetSearchOptionObject

swDmSearchOpt.ClearAllSearchPaths()

swDmSearchOpt.AddSearchPath(" public_documents \SOLIDWORKS\SOLIDWORKS
2024\samples\tutorial\advdrawings ")

DimdOpenDocsAsNewScripting.Dictionary

DimswDoc12AsSwDMDocument12

DimresAsSwDmDocumentOpenError

DimdtAsSwDmDocumentType

dt = SwDmDocumentType.swDmDocumentAssembly

DimfilenameAsString

filename =" public_documents \SOLIDWORKS\SOLIDWORKS
2024\samples\tutorial\advdrawings\98food processor.SLDASM"

swDoc12 = swDocMgr.GetDocument(filename, dt,False, res)

IfswDoc12IsNothingOr(res <> SwDmDocumentOpenError.swDmDocumentOpenErrorNone)Then

Debug.Print("Error
opening file...")

ExitSub

EndIf

dOpenDocs.Add(filename, swDoc12)

DimactiveConfigAsSwDMConfiguration8

DimconfigMgrAsSwDMConfigurationMgr

configMgr = swDoc12.ConfigurationManager

DimvConfigNamesAsObject

vConfigNames = configMgr.GetConfigurationNames

DimjAsInteger

Debug.Print("Assembly
configurations: ")

Forj = 0ToUBound(vConfigNames)

Debug.Print(" "& vConfigNames(j))

Nextj

Debug.Print("Get
the active assembly configuration...")

DimsActiveConfigAsString

sActiveConfig = configMgr.GetActiveConfigurationName

activeConfig = configMgr.GetConfigurationByName(sActiveConfig)

IfactiveConfigIsNothingThen

Debug.Print("Error
getting the active assembly configuration...")

Return

EndIf

Debug.Print("The
active assembly configuration is "& sActiveConfig)

Debug.Print("Get
the components of the active assembly configuration...")

DimvComponentsAsObject

vComponents = activeConfig.GetComponents

DimswDmComponentAsSwDMComponent12

DimiAsInteger

Fori = 0ToUBound(vComponents)

swDmComponent = vComponents(i)

Debug.Print("")

Debug.Print("Component
name = "& swDmComponent.Name3 &" Config = "& swDmComponent.ConfigurationName)

DimswDmCompDocCurAsSwDMDocument

DimlErrAsInteger

DimbIsInDictAsBoolean

bIsInDict = dOpenDocs.Exists(swDmComponent.Name)

IfNotbIsInDictThen

swDmCompDocCur = swDmComponent.GetDocument2(False, swDmSearchOpt, lErr)

IfNotswDmCompDocCurIsNothingThen

dOpenDocs.Add(swDmComponent.Name, swDmCompDocCur)

EndIf

Else

swDmCompDocCur = dOpenDocs(swDmComponent.Name)

EndIf

DimvCustomPropNamesFromDocAsObject

DimlPropTypeAsInteger

DimsPropValAsString

DimkAsInteger

IfswDmCompDocCurIsNotNothingThen

Debug.Print("*********
Document-level custom properties **************")

vCustomPropNamesFromDoc = swDmCompDocCur.GetCustomPropertyNames()

IfvCustomPropNamesFromDocIsNotNothingThen

Fork = 0ToUBound(vCustomPropNamesFromDoc)

sPropVal = swDmCompDocCur. GetCustomProperty (vCustomPropNamesFromDoc(k),
lPropType)

Debug.Print(vCustomPropNamesFromDoc(k) &": Value: "& sPropVal &", Type: "& lPropType)

Nextk

Debug.Print("*********
Component-level custom properties **************")

DimmAsInteger

Form = 0ToUBound(vCustomPropNamesFromDoc)

sPropVal = swDmComponent. GetCustomProperty (vCustomPropNamesFromDoc(m),
lPropType)

Debug.Print(vCustomPropNamesFromDoc(m) &": Value: "& sPropVal &", Type: "& lPropType)

Nextm

DimswDmCompDocCurConfigMgrAsSwDMConfigurationMgr

swDmCompDocCurConfigMgr
= swDmCompDocCur.ConfigurationManager

DimswDmCompDocCurConfigMgr2AsSwDMConfigurationMgr2

swDmCompDocCurConfigMgr2 = swDmCompDocCurConfigMgr

DimswDmCompConfigCurAsSwDMConfiguration

DimswDmCompConfigCur14AsSwDMConfiguration14

DimswDmConfigErrAsSwDMConfigurationError

swDmCompConfigCur =
swDmCompDocCurConfigMgr2.GetConfigurationByName2(swDmComponent.ConfigurationName,
swDmConfigErr)

swDmCompConfigCur14 = swDmCompConfigCur

DimlCustPropCountAsInteger

lCustPropCount = swDmCompConfigCur.GetCustomPropertyCount

DimvCustPropNamesAsObject

vCustPropNames = swDmCompConfigCur.GetCustomPropertyNames

Debug.Print("*********
Configuration-level custom properties **************")

IflCustPropCount > 0Then

DimrAsInteger

Forr = 0ToUBound(vCustPropNames)

sPropVal = swDmCompConfigCur. GetCustomProperty (vCustPropNames(r),
lPropType)

Debug.Print(vCustPropNames(r) &": "& sPropVal &", "& lPropType)

Nextr

Else

Debug.Print("None")

EndIf

Else

Debug.Print("None")

EndIf

EndIf

Next

DimsAsInteger

DimswDmDocCurAsSwDMDocument

Fors = 0TodOpenDocs.Count - 1

swDmDocCur = dOpenDocs.Items()(s)

swDmDocCur.CloseDoc()

swDmDocCur =Nothing

Nexts

dOpenDocs.RemoveAll

dOpenDocs =Nothing

EndSub

EndModule
