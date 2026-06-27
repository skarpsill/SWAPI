---
title: "FeatureManager::FeatureLinearPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__FeatureLinearPattern.htm"
---

# FeatureManager::FeatureLinearPattern

This method is obsolete and has been superseded
by[FeatureManager::FeatureLinearPattern2](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureLinearPattern2.htm).

Description

This method inserts a linear
pattern feature of the selected features or components.

Syntax (OLE Automation)

retval = FeatureManager.FeatureLinearPattern ( num1,
spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2 )

(Table)=========================================================

| Input: | (long) num1 | Number of instances of the linear pattern in Direction 1, including
the original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing between each instance of the linear pattern in Direction 1 in
meters |
| Input: | (long) num2 | Number of instances of the linear pattern in Direction 2, including
the original |
| Input: | (double) spacing2 | Spacing between each instance of the linear pattern in Direction 2 in
meters |
| Input: | (VARIANT_BOOL) flipDir1 | TRUE if you want to reverse the direction the linear pattern in Direction
1, FALSE if not |
| Input: | (VARIANT_BOOL) flipDir2 | TRUE if you want to reverse the direction of the linear pattern in Direction
2, FALSE if not |
| Input: | (BSTR) dName1 | Name of the dimension defining Direction 1 |
| Input: | (BSTR) dName2 | Name of the dimension defining in Direction 2 |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->FeatureLinearPattern
( num1, spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2,
retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) num1 | Number of instances of the linear pattern in Direction 1, including
the original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing between each instance of the linear pattern in Direction 1 in
meters |
| Input: | (long) num2 | Number of instances of the linear pattern in Direction 2, including
the original |
| Input: | (double) spacing2 | Spacing between each instance of the linear pattern in Direction 2,
meters |
| Input: | (VARIANT_BOOL) flipDir1 | TRUE if you want to reverse the direction the linear pattern in Direction
1 |
| Input: | (VARIANT_BOOL) flipDir2 | TRUE if you want to reverse the direction of the linear pattern in Direction
2, FALSE if not |
| Input: | (BSTR) dName1 | Name of the dimension defining Direction 1 |
| Input: | (BSTR) dName2 | Name of the dimension defining Direction 2 |
| Output: | (LPFEATURE) *retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires ordered selection of the features
and components.

- Features.
  Use ModelDocExtension::SelectByID 1 and 2 for the directions and ModelDocExtension::SelectByID
  4 for the features to pattern.
- Components.
  Use ModelDocExtension::SelectByID 1 for the components to pattern and
  ModelDocExtension::SelectByID 2 and 4 for the directions.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__FeatureLinearPattern.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__FeatureLinearPattern.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
