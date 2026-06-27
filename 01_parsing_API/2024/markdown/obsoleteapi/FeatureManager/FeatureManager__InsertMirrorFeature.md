---
title: "FeatureManager::InsertMirrorFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertMirrorFeature.htm"
---

# FeatureManager::InsertMirrorFeature

This method is obsolete and has been superseded
by[FeatureManager::InsertMirrorFeature2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMirrorFeature2.htm).

Description

This method mirrors selected features, faces,
and bodies about a selected plane or planar face.

Syntax (OLE Automation)

retval = FeatureManager.InsertMirrorFeature ( bMirrorBody,
bGeometryPattern, bMerge, bKnit )

(Table)=========================================================

| Input: | (VARIANT_BOOL) bMirrorBody | TRUE to mirror solid bodies; FALSE to mirror a feature or face |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) bGeometryPattern | TRUE to mirror only the feature geometry, FALSE to solve the entire
feature; applies to mirroring features only |
| Input: | (VARIANT_BOOL) bMerge | TRUE to merge any mirrored solid bodies, FALSE to not; applies to mirroring
solid bodies only |
| Input: | (VARIANT_BOOL) bKnit | TRUE to knit surfaces, FALSE to not; applies to mirroring surfaces only |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertMirrorFeature (
bMirrorBody, bGeometryPattern, bMerge, bKnit, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (VARIANT_BOOL) bMirrorBody | TRUE to mirror solid bodies; FALSE to mirror a feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) bGeometryPattern | TRUE to mirror only the feature geometry, FALSE to solve the entire
feature; applies to mirroring features only |
| Input: | (VARIANT_BOOL) bMerge | TRUE to merge the solid bodies, FALSE to not; applies to mirroring solid
bodies only |
| Input: | (VARIANT_BOOL) bKnit | TRUE to knit surfaces, FALSE to not; applies to mirroring surfaces only |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method attempts to create the mirror feature
without displaying a dialog box to get information from the user. It relies
on preselected and marked entities, as well as arguments.

(Table)=========================================================

| Any... | Must be preselected and marked with a value
of... |
| --- | --- |
| Features to be mirrored | 1 |
| Faces to be mirrored | 128 |
| Bodies to be mirrored | 256 |
| Plane or planar face | 2 |

For information on selecting and marking entities,
refer to ModelDocExtension::SelectByID2.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\FeatureManager\FeatureManager__InsertMirrorFeature.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\FeatureManager\FeatureManager__InsertMirrorFeature.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
