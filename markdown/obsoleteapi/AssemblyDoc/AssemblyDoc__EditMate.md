---
title: "AssemblyDoc::EditMate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__EditMate.htm"
---

# AssemblyDoc::EditMate

This method is obsolete and has been superseded
by[AssemblyDoc::EditMate2](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__EditMate2.htm).

Description

This method edits the selected assembly component mate relationship.

Syntax (OLE Automation)

void AssemblyDoc.EditMate ( mateType,
align, flip, dist, angle)

(Table)=========================================================

| Input: | (long) mateType | Type of mate as defined in swMateType_e |
| --- | --- | --- |
| Input: | (long) align | Type of alignment desired as defined in swMateAlign_e |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the component, FALSE to not |
| Input: | (double) dist | Distance value used with swMateDISTANCE mate type |
| Input: | (double) angle | Angle value used with swMateANGLE mate type |

Syntax (COM)

status = AssemblyDoc->EditMate (
mateType, align, flip, dist, angle )

(Table)=========================================================

| Input: | (long) mateType | Type of mate as defined in swMateType_e |
| --- | --- | --- |
| Input: | (long) align | Type of alignment desired as defined in swMateAlign_e |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the component, FALSE to not |
| Input: | (double) dist | Distance value used with swMateDISTANCE mate type |
| Input: | (double) angle | Angle value used with swMateANGLE mate type |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The first selection should be the two items that are mated (that is,
two faces, edge and face, and so on), and the third selection should be
the mate feature to be edited.

If mateType is swMateDISTANCE or swMateANGLE when the mate is applied
to the closest position that meets the mate condition specified by dist
or angle, then setting flip to TRUE jumps the assembly to the other possible
mate position.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$ZMateRelationShips$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDoc\AssemblyDoc__EditMate.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
