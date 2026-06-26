---
title: "Suppress Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Suppress_Feature_Example_VB.htm"
---

# Suppress Feature Example (VBA)

This example shows how to suppress the selected feature.

'------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part or assembly is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
At least one entity is selected.

'

' Postconditions: All features associated with the selected

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}entities
are suppressed.

'

' NOTE: Features are only suppressed if

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
owning feature exists for that entity.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
typically occurs for edges.

'

'-------------------------------------------

Option Explicit

Public Enum swSelectType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelNOTHING
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEDGES
= 1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EDGE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelFACES
= 2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"FACE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelVERTICES
= 3kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"VERTEX"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDATUMPLANES
= 4kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"PLANE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDATUMAXES
= 5kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"AXIS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDATUMPOINTS
= 6kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DATUMPOINT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelOLEITEMS
= 7kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"OLEITEM"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelATTRIBUTES
= 8kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"ATTRIBUTE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHES
= 9kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCH"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHSEGS
= 10kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCHSEGMENT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHPOINTS
= 11kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCHPOINT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDRAWINGVIEWS
= 12kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DRAWINGVIEW"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelGTOLS
= 13kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"GTOL"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDIMENSIONS
= 14kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DIMENSION"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelNOTES
= 15kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"NOTE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSECTIONLINES
= 16kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SECTIONLINE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDETAILCIRCLES
= 17kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DETAILCIRCLE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSECTIONTEXT
= 18kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SECTIONTEXT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSHEETS
= 19kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SHEET"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCOMPONENTS
= 20kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"COMPONENT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMATES
= 21kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"MATE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBODYFEATURES
= 22kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BODYFEATURE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREFCURVES
= 23kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"REFCURVE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEXTSKETCHSEGS
= 24kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EXTSKETCHSEGMENT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEXTSKETCHPOINTS
= 25kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EXTSKETCHPOINT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelHELIX
= 26kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"HELIX"
(is this wrong?)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREFERENCECURVES
= 26kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"REFERENCECURVES"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREFSURFACES
= 27kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"REFSURFACE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCENTERMARKS
= 28kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"CENTERMARKS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelINCONTEXTFEAT
= 29kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"INCONTEXTFEAT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMATEGROUP
= 30kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"MATEGROUP"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBREAKLINES
= 31kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BREAKLINE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelINCONTEXTFEATS
= 32kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"INCONTEXTFEATS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMATEGROUPS
= 33kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"MATEGROUPS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHTEXT
= 34kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCHTEXT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSFSYMBOLS
= 35kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SFSYMBOL"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDATUMTAGS
= 36kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DATUMTAG"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCOMPPATTERN
= 37kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"COMPPATTERN"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelWELDS
= 38kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"WELD"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCTHREADS
= 39kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"CTHREAD"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDTMTARGS
= 40kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DTMTARG"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelPOINTREFS
= 41kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"POINTREF"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDCABINETS
= 42kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DCABINET"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEXPLVIEWS
= 43kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EXPLODEDVIEWS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEXPLSTEPS
= 44kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EXPLODESTEPS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEXPLLINES
= 45kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EXPLODELINES"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSILHOUETTES
= 46kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SILHOUETTE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCONFIGURATIONS
= 47kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"CONFIGURATIONS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelOBJHANDLES
= 48

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelARROWS
= 49kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"VIEWARROW"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelZONES
= 50kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"ZONES"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREFEDGES
= 51kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"REFERENCE-EDGE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREFFACES
= 52

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREFSILHOUETTE
= 53

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBOMS
= 54kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BOM"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEQNFOLDER
= 55kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EQNFOLDER"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHHATCH
= 56kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCHHATCH"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelIMPORTFOLDER
= 57kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"IMPORTFOLDER"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelVIEWERHYPERLINK
= 58kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"HYPERLINK"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMIDPOINTS
= 59

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCUSTOMSYMBOLS
= 60kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"CUSTOMSYMBOL"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCOORDSYS
= 61kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"COORDSYS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDATUMLINES
= 62kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"REFLINE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelROUTECURVES
= 63

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBOMTEMPS
= 64kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BOMTEMP"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelROUTEPOINTS
= 65kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"ROUTEPOINT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCONNECTIONPOINTS
= 66kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"CONNECTIONPOINT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelROUTESWEEPS
= 67

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelPOSGROUP
= 68kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"POSGROUP"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBROWSERITEM
= 69kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BROWSERITEM"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelFABRICATEDROUTE
= 70kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"ROUTEFABRICATED"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHPOINTFEAT
= 71kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCHPOINTFEAT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEMPTYSPACE
= 72kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(is this
wrong?)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCOMPSDONTOVERRIDE
= 72

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelLIGHTS
= 73kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"LIGHTS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelWIREBODIES
= 74

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSURFACEBODIES
= 75kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SURFACEBODY"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSOLIDBODIES
= 76kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SOLIDBODY"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelFRAMEPOINT
= 77kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"FRAMEPOINT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSURFBODIESFIRST
= 78

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMANIPULATORS
= 79kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"MANIPULATOR"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelPICTUREBODIES
= 80kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"PICTURE
BODY"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSOLIDBODIESFIRST
= 81

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelDOWELSYMS
= 86kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"DOWELSYM"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEXTSKETCHTEXT
= 88kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"EXTSKETCHTEXT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBLOCKINST
= 93kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BLOCKINST"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelFTRFOLDER
= 94kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"FTRFOLDER"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHREGION
= 95kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCHREGION"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSKETCHCONTOUR
= 96kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SKETCHCONTOUR"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBOMFEATURES
= 97kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BOMFEATURE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelANNOTATIONTABLES
= 98kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"ANNOTATIONTABLES"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBLOCKDEF
= 99kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BLOCKDEF"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCENTERMARKSYMS
= 100kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"CENTERMARKSYMS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelCENTERLINES
= 103kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"CENTERLINE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelHOLETABLEFEATS
= 104kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"HOLETABLE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelHOLETABLEAXES
= 105kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"HOLETABLEAXIS"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelWELDMENT
= 106kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"WELDMENT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelSUBWELDFOLDER
= 107kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"SUBWELDMENT"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEXCLUDEMANIPULATORS
= 111

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREVISIONTABLE
= 113kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"REVISIONTABLE"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelBODYFOLDER
= 118kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"BDYFOLDER"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelREVISIONTABLEFEAT
= 119

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEVERYTHING
= -3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelLOCATIONS
= -2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelUNSUPPORTED
= -1

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelEVERYTHING
= 4294967293

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelLOCATIONS
= 4294967294

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelUNSUPPORTED
= 4294967295

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}On
Error Resume Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Information about selected entities

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 1 To swSelMgr.GetSelectedObjectCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelMgr.GetSelectedObject5(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelType("
& i & ") = " & swSelMgr.GetSelectedObjectType(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not swFeat Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swFeat.Name& "
<" & swFeat.GetTypeName& ">"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Suppress what has been selected

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swModel.EditSuppress2: Debug.Assert
bRet

End Sub

'------------------------------------------
