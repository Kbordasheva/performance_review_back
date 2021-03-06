from rest_framework import serializers

from core.serializers import DynamicFieldsSerializer
from employee.serializers import EmployeeListSerializer, EmployeeSerializer


class CommentSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    author = serializers.CharField(read_only=True)
    text = serializers.CharField(max_length=1000)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class CriteriaSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=1000)
    is_done = serializers.BooleanField()
    start_date = serializers.DateField(allow_null=True, required=False)
    deadline = serializers.DateField(allow_null=True, required=False)
    finish_date = serializers.DateField(allow_null=True, required=False)


class GoalSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=1000)
    is_done = serializers.BooleanField(read_only=True)
    criteria = CriteriaSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


class GoalMarkDoneSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    is_done = serializers.BooleanField()


class PerformanceReviewSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    employee = EmployeeListSerializer()
    year = serializers.IntegerField(min_value=2000, max_value=2050)
    goals_count = serializers.SerializerMethodField()
    goals_done_count = serializers.SerializerMethodField()

    def get_goals_count(self, performance_review):
        return performance_review.goals.count()

    def get_goals_done_count(self, performance_review):
        return performance_review.goals.filter(is_done=True).count()


class PerformanceReviewDetailsSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField(min_value=2000, max_value=2050)
    goals = GoalSerializer(many=True, read_only=True)


class EmployeeProfileSerializer(EmployeeSerializer):
    review = PerformanceReviewDetailsSerializer(many=True)


class PerformanceReviewCreateSerializer(DynamicFieldsSerializer):
    id = serializers.IntegerField(read_only=True)
    employee_id = serializers.IntegerField()
    year = serializers.IntegerField(min_value=2000, max_value=2050)
