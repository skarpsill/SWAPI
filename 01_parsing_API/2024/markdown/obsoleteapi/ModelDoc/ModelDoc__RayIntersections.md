---
title: "ModelDoc::RayIntersections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__RayIntersections.htm"
---

# ModelDoc::RayIntersections

This
method is obsolete and has been superseded by[ModelDoc2::RayIntersections](sldworksAPI.chm::/ModelDoc2/ModelDoc2__RayIntersections.htm).

Description

This method intersects a given set of rays
with a specified set of bodies. The resulting information, a set of intersection
points, intersection normals, and the bodies that were hit from your bodiesInarray, can be retrieved by calling
ModelDoc::GetRayIntersectionsPoints and ModelDoc::GetRayIntersectionsTopology.

Syntax (OLE Automation)

retval = ModelDoc.RayIntersections (bodiesIn, basePointsIn, vectorsIn, options, hitRadius,
offset)

(Table)=========================================================

| Input: | (VARIANT) bodiesIn | SafeArray of Dispatch pointers; these are the
Body objects that will be hit by the rays |
| --- | --- | --- |
| Input: | (VARIANT) basePointsIn | SafeArray of doubles containing the x,y,z base
points of each ray |
| Input: | (VARIANT) vectorsIn | SafeArray of doubles containing the direction
vectors of each ray |
| Input: | (long) options | Any number of options as defined in swRayPtsOpts_e;
concatenate any options using the "or" operator. |
| Input: | (double) hitRadius | Radius of hit cylinder; this is used mainly in
grazing cases to establish a hit |
| Input: | (double) offset | Length tolerance to use to establish whether
a hit on a face represents the entry or exit of the ray from the body |
| Return: | (long) retval | Number of intersections found |

Syntax (COM)

status = ModelDoc->IRayIntersections
( bodiesIn, numBodies, basePointsIn, vectorsIn, numRays, options, hitRadius,
offset, &retval )

(Table)=========================================================

| Input: | (LPBODY*) bodiesIn | Array of pointers to the Body objects; these
are the Body objects that will be hit by the rays |
| --- | --- | --- |
| Input: | (long) numBodies | Number of bodies in the bodiesIn array |
| Input: | (double*) basePointsIn | Array containing the x,y,z base points of each
ray |
| Input: | (double*) vectorsIn | Array containing the direction vectors of each
ray |
| Input: | (long) numRays | Number of rays specified; this should be equal
to the number of elements in the (basePointsIn / 3) or (vectorsIn / 3)
arrays |
| Input: | (long) options | Any number of options selected as defined in
swRayPtsOpts_e; concatenate these options using the "or" operator |
| Input: | (double) hitRadius | Radius of hit cylinder used mainly in grazing
cases to establish a hit |
| Input: | (double) offset | Length tolerance to use to establish whether
a hit on a face represents the entry or exit of the ray from the body |
| Output: | (long) retval | Number of intersections found |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The method performs the intersection operations
between the specified bodies and the ray vectors provided. To get the
results of the intersection operations, you must call ModelDoc::GetRayIntersectionsPoints
and ModelDoc::GetRayIntersectionsTopology.

Information returned by ModelDoc::GetRayIntersectionsPoints
and ModelDoc::GetRayIntersectionsTopology depends partially on the value
of the options argument. Valid values, which can take values from the
swRayPtsOpts_e enumerator, can be concatenated together using bitwise
operations. Refer to ModelDoc::GetRayIntersectionsPoints to see which
data is always output regardless of the values specified in the options
argument.

For the COM interface, the return value, the intersection
count, must be used in determining the size of arrays to allocate for
return values from ModelDoc::GetRayIntersectionsPoints and ModelDoc::GetRayIntersectionsTopology.

For each ray that hits an edge or a vertex, theoffsetdistance is added in both
the positive and negative directions along the ray and the points computed
will be tested for spatial inclusion in the hit body. This will be used
to determine if the ray was entering, leaving, or just grazing the body
at the hit point. Entry and exit onto faces can be computed more simply
and does not require such an offset.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZTessellation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__RayIntersections.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
