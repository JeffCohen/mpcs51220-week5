// C# example, violation of Open-Closed Principle

public interface IEmployee
{
  void SignContract();
}

class Engineer : IEmployee
{

}
class Manager : IEmployee
{

}
class SalesPerson : IEmployee
{

}
public class HumanResourceDepartment
{
    private IList<IEmployee> _hiredPeople;

    public void Hire(IEmployee person){
        person.SignContract();
        _hiredPeople.Add(person);
    }
}

// What about architects? etc..

// public class HumanResourceDepartment
// {
//     private IList<IEmployee> _employees;
//     public void Hire(IEmployee employee)
//     {
//         employee.SignContract();
//         _employees.Add(employee);
//     }
// }
