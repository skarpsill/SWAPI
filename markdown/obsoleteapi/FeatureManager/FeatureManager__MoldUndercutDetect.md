---
title: "FeatureManager::MoldUndercutDetect"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__MoldUndercutDetect.htm"
---

# FeatureManager::MoldUndercutDetect

This method is obsolete and has been superseded
by[FeatureManager::MoldUndercutDetect2](sldworksAPI.chm::/FeatureManager/FeatureManager__MoldUndercutDetect2.htm).

Description

This method detects undercut
features.

Syntax (OLE Automation)

void = FeatureManager.MoldUndercutDetect ( colUndercut,
colBase, bCoordInput, dX, dY, dZ)

(Table)=========================================================

| Input: | (long) colUndercut | Value (COLORREF type) that specifies
the color for the faces that form an undercut |
| --- | --- | --- |
| Input: | (long) colBase | Value (COLORREF type) that specifies the color
for the faces that do not form undercuts, that is, all faces except the
undercut faces |
| Input: | (VARIANT_BOOL) bCoordInput | TRUE to enable coordinate input, FALSE to not |
| Input: | (double) dX | X coordinate |
| Input: | (double) dY | Y coordinate |
| Input: | (double) dZ | Z coordinate |

Syntax (COM)

status = FeatureManager->MoldUndercutDetect (
colUndercut, colBase, bCoordInput, dX, dY, dZ)

Parameters Table Start

(Table)=========================================================

| Input: | (long) colUndercut | Value (COLORREF type) that specifies the color
for the faces that form an undercut |
| --- | --- | --- |
| Input: | (long) colBase | Value (COLORREF type) that specifies the color
for the faces that do not form undercuts, that is, all faces except the
undercut faces |
| Input: | (VARIANT_BOOL) bCoordInput | TRUE to enable coordinate input,
FALSE to not |
| Input: | (double) dX | X coordinate |
| Input: | (double) dY | Y coordinate |
| Input: | (double) dZ | Z coordinate |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__MoldUndercutDetect.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__MoldUndercutDetect.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
