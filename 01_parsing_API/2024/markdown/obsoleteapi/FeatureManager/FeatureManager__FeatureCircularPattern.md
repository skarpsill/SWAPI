---
title: "FeatureManager::FeatureCircularPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__FeatureCircularPattern.htm"
---

# FeatureManager::FeatureCircularPattern

This method is obsolete and has been superseded
by[FeatureManager::FeatureCircularPattern2](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureCircularPattern2.htm).

Description

This method inserts a circular
pattern feature in the selected features or components.

Syntax (OLE Automation)

retval = FeatureManager.FeatureCircularPattern (
num, spacing, flipDir, dName )

(Table)=========================================================

| Input: | (long) num | Number of instances of the circular pattern to insert, including the
original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing between each instance of the circular pattern in radians |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction of the circular pattern |
| Input: | (BSTR) dName | Name of the angular dimension defining the direction of the pattern |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->FeatureCircularPattern
( num, spacing, flipDir, dName, retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) num | Number of instances of the circular pattern to insert, including the
original |
| --- | --- | --- |
| Input: | (double) spacing | Spacing between each instance of the circular pattern in radians |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction of the circular pattern |
| Input: | (BSTR) dName | Name of the angular dimension defining the direction of the pattern |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires ordered selection of the features and components.

- Features.
  Use ModelDocExtension::SelectByID 4 for the features to pattern.
- Components.
  Use ModelDocExtension::SelectByID 1 for the components to pattern and
  ModelDocExtension::SelectByID 2 for the axis.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__FeatureCircularPattern.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$Feature_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__FeatureCircularPattern.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
