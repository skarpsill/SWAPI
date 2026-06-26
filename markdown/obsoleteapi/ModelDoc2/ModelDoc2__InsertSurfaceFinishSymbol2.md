---
title: "ModelDoc2::InsertSurfaceFinishSymbol2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSurfaceFinishSymbol2.htm"
---

# ModelDoc2::InsertSurfaceFinishSymbol2

This method is obsolete and has been superseded
by[ModelDocExtension::InsertSurfaceFinishSymbol3](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__InsertSurfaceFinishSymbol3.htm).

Description

This method creates a surface-finish symbol based on the last selection.

Syntax (OLE Automation)

retval = ModelDoc2.InsertSurfaceFinishSymbol2
( symType, leaderType, locX, locY, locZ, laySymbol, arrowType, machAllowance,
otherVals, prodMethod, sampleLen, maxRoughness, minRoughness, roughnessSpacing)

(Table)=========================================================

| Input: | (long) symType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Input: | (long) leaderType | Leader type as defined in swLeaderStyle_e |
| Input: | (double) locX | X location for symbol |
| Input: | (double) locY | Y location for symbol |
| Input: | (double) locZ | Z location for symbol |
| Input: | (long) laySymbol | Direction of lay as defined in swSFLaySym_e |
| Input: | (long) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (BSTR) machAllowance | Material removal allowance |
| Input: | (BSTR) otherVals | Other roughness values |
| Input: | (BSTR) prodMethod | Production method and treatment |
| Input: | (BSTR) sampleLen | Sampling length |
| Input: | (BSTR) maxRoughness | Maximum roughness |
| Input: | (BSTR) minRoughness | Minimum roughness |
| Input: | (BSTR) roughnessSpacing | Roughness spacing |
| Return: | (BOOL) retval | TRUE if the finish symbol is inserted successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->InsertSurfaceFinishSymbol2
( symType, leaderType, locX, locY, locZ, laySymbol, arrowType, machAllowance,
otherVals, prodMethod, sampleLen, maxRoughness, minRoughness, roughnessSpacing,
&retval )

(Table)=========================================================

| Input: | (long) symType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Input: | (long) leaderType | Leader type as defined in swLeaderStyle_e |
| Input: | (double) locX | X location for symbol |
| Input: | (double) locY | Y location for symbol |
| Input: | (double) locZ | Z location for symbol |
| Input: | (long) laySymbol | Direction of lay as defined in swSFLaySym_e |
| Input: | (long) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (BSTR) machAllowance | Material removal allowance |
| Input: | (BSTR) otherVals | Other roughness values |
| Input: | (BSTR) prodMethod | Production method/treatment |
| Input: | (BSTR) sampleLen | Sampling length |
| Input: | (BSTR) maxRoughness | Maximum roughness |
| Input: | (BSTR) minRoughness | Minimum roughness |
| Input: | (BSTR) roughnessSpacing | Roughness spacing |
| Output: | (VARIANT_BOOL) retval | TRUE if the finish symbol is inserted successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The SolidWorks software uses the location
parameters for this method only if the surface finish symbol has a leader– leaderType
!= swNO_LEADER.

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertSurfaceFinishSymbol2.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertSurfaceFinishSymbol2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
