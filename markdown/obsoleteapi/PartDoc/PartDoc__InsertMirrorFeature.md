---
title: "PartDoc::InsertMirrorFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__InsertMirrorFeature.htm"
---

# PartDoc::InsertMirrorFeature

This method is obsolete and has been superseded
by[FeatureManager::InsertMirrorFeature](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertMirrorFeature.htm).

Description

This method mirrors selected features and faces
about a selected plane or planar face.

Syntax (OLE Automation)

retval = PartDoc.InsertMirrorFeature ( GeometryPattern
)

(Table)=========================================================

| Input: | (BOOL) GeometryPattern | TRUE to mirror only the feature geometry, FALSE
to solve the entire feature |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the feature is successfully created, FALSE if not |

Syntax (COM)

status = PartDoc->InsertMirrorFeature ( GeometryPattern,
&retval )

Parameters Table Start

(Table)=========================================================

| Input: | (VARIANT_BOOL) GeometryPattern | TRUE to mirror only the feature geometry, FALSE
to solve the entire feature |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the feature is successfully created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Unlike PartDoc::MirrorFeature, this method tries
to create the mirror feature without displaying a dialog box to get information
from the end-user. It relies on preselected and marked entities and arguments.

- Any features
  to be mirrored must be preselected and marked with a value of 1.
- Any faces
  to be mirrored must be preselected and marked with a value of 128.
- The plane
  or planar face to mirror about needs must be preselected and marked with
  a value of 2.

For information on selecting and marking entities,
see ModelDocExtension::SelectByID.

This method returns a TRUE or FALSE to indicate
whether or not the mirror all feature was created. If it is successful,
the newly created feature remains selected after the method runs. You
can use SelectionMgr::GetSelectedObject3 to retrieve this object.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\PartDoc\PartDoc__InsertMirrorFeature.htm" >
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
<param name="Items" value="PartDoc Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\PartDoc\PartDoc__InsertMirrorFeature.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
