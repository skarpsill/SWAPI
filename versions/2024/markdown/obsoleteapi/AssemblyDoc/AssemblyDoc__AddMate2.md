---
title: "AssemblyDoc::AddMate2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__AddMate2.htm"
---

# AssemblyDoc::AddMate2

This method is obsolete and has been superseded
by[AssemblyDoc::AddMate3](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__AddMate3.htm).

Description

This method adds a mate relationship
to the selected entities.

Syntax (OLE Automation)

pMateObjOut = AssemblyDoc.AddMate2 ( mateTypeFromEnum,
alignFromEnum, flip, distance, distAbsUpperLimit, distAbsLowerLimit, gearRatioNumerator,
gearRatioDenominator, angle, angleAbsUpperLimit, angleAbsLowerLimit, errorStatus
)

(Table)=========================================================

| Input: | (long) mateTypeFromEnum | Type of mate as defined in swMateType_e |
| --- | --- | --- |
| Input: | (long) alignFromEnum | Type of alignment as defined in swMateAlign_e |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the component, FALSE otherwise |
| Input: | (double) distance | Distance value to use with distance or limit mates |
| Input: | (double) distAbsUpperLimit | Absolute maximum distance value (see Remarks ) |
| Input: | (double) distAbsLowerLimit | Absolute minimum distance value (see Remarks ) |
| Input: | (double) gearRatioNumerator | Gear ratio numerator value for gear mates |
| Input: | (double) gearRatioDenominator | Gear ratio denominator value for gear mates |
| Input: | (double) angle | Angle value to use with angle mates |
| Input: | (double) angleAbsUpperLimit | Absolute maximum angle value |
| Input: | (double) angleAbsLowerLimit | Absolute minimum angle value |
| Output: | (long) errorStatus | Success or error as defined by swAddMateError_e |
| Output: | (LPMATE2) pMateObjOut | Pointer to the Mate2 object |

Syntax (COM)

status = AssemblyDoc->AddMate2 ( mateTypeFromEnum,
alignFromEnum, flip, distance, distAbsUpperLimit, distAbsLowerLimit, gearRatioNumerator,
gearRatioDenominator, angle, angleAbsUpperLimit, angleAbsLowerLimit, errorStatus,
&pMateObjOut )

Parameters Table Start

(Table)=========================================================

| Input: | (long) mateTypeFromEnum | Type of mate as defined in swMateType_e |
| --- | --- | --- |
| Input: | (long) alignFromEnum | Type of alignment as defined in swMateAlign_e |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the component, FALSE otherwise |
| Input: | (double) distance | Distance value to use with distance or limit mates |
| Input: | (double) distAbsUpperLimit | Absolute maximum distance value (see Remarks ) |
| Input: | (double) distAbsLowerLimit | Absolute minimum distance value (see Remarks ) |
| Input: | (double) gearRatioNumerator | Gear ratio numerator value for gear mates |
| Input: | (double) gearRatioDenominator | Gear ratio denominator value for gear mates |
| Input: | (double) angle | Angle value to use with angle mates |
| Input: | (double) angleAbsUpperLimit | Absolute maximum angle value |
| Input: | (double) angleAbsLowerLimit | Absolute minimum angle value |
| Output: | (long) errorStatus | Success or error as defined by swAddMateError_e |
| Output: | (LPMATE2) pMateObjOut | Pointer to the Mate2 object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To specify a distance mate
without limits, set the distAbsUpperLimit and distAbsLowerLimit arguments
equal to the distance argument's value.

If mateTypeFromEnum is swMateDISTANCE
or swMateANGLE when the mate is applied to the closest position that meets
the mate condition specified by distance or angle, then setting flip to
TRUE moves the assembly to the other possible mate position.

Use:

- ModelDoc2::ClearSelection2(VARIANT_TRUE)
  before selecting entities to mate.
- ModelDocExtension::SelectByID2
  with Mark = 1 to select entities to mate.
- ModelDoc2::ClearSelection2(VARIANT_TRUE)
  after the mate is created.

If mateTypeFromEnum is swMateCAMFOLLOWER,
then use a selection mark of 8 for the cam-follower face.

If nothing is preselected, then errorStatus
is swAddMateError_IncorrectSeletions and pMateObjOut is NULL/Nothing.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\AssemblyDoc\AssemblyDoc__AddMate2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$AssemblyDocMate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\AssemblyDoc\AssemblyDoc__AddMate2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXAddMates$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\AssemblyDoc\AssemblyDoc__AddMate2.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
